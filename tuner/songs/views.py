import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view
from tuner.songs.similarities import cosine_similarity, jaccards_coefficient

songs_df = pd.read_csv("https://media.githubusercontent.com/media/diego-codes/tuner/master/data/songs.csv", index_col="spotify_id")
song_top_20_sims = pd.read_csv("https://media.githubusercontent.com/media/diego-codes/tuner/master/data/top-20-sims.csv", index_col="spotify_id")

features = pd.read_csv("https://media.githubusercontent.com/media/diego-codes/tuner/master/data/features.csv")["0"]
genres = pd.read_csv("https://media.githubusercontent.com/media/diego-codes/tuner/master/data/genres.csv")["0"]
songs = [{
  "id": id, 
  "title": s.title, 
  "artist": s.artist
  } for id, s in songs_df[["title", "artist"]].iterrows()]


@api_view()
def get_songs(request):
  return Response(songs)

@api_view()
def similar_songs(request, id):
  return Response([song_id for idx, song_id in song_top_20_sims.loc[id].iteritems()])

@api_view(['POST'])
def get_recommendations(request):
  ratings = pd.Series(request.data)

  rocchios_pos_weight = 0.75
  rocchios_neg_weight = 0.25
  weighted_song_ratings = ratings
  weighted_song_ratings[weighted_song_ratings == 1] *= rocchios_pos_weight
  weighted_song_ratings[weighted_song_ratings == -1] *= rocchios_neg_weight
  weighted_song_ratings

  user_profile = songs_df.loc[ratings.index][[*features, *genres]].multiply(weighted_song_ratings, axis=0).sum()

  feature_sims = cosine_similarity(user_profile[features], songs_df.drop(ratings.index)[features])
  genres_sims = jaccards_coefficient(user_profile[genres], songs_df.drop(ratings.index)[genres])

  # Weight the genre scores against the features score.
  weight = 0.01
  sims = (feature_sims * (1 - weight) + genres_sims * weight)
  return Response([{ "id": id, "score": score } for id, score in sims.sort_values().tail(10).iteritems()])
