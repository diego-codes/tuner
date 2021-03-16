# Tuner API server

This API server recommends songs to users based on their ratings.

## How to run locally

### Requirements

To run this server locally, you will need Python3 and `pip` installed.

### Install dependencies

Install dependencies with the following command:

```
pip install -r requirements.txt
```

### Run the migrations

This project uses Django, so you need to run the migrations to get started:

```
python manage.py migrate
```

### Run the server

Finally, you can run the web server with the following command:

```
python manage.py runserver
```

It might take a few seconds to boot up, but once it is ready, you can access it via your browser at http://localhost:8000/.

## Endpoints

### `GET /songs`

Get the full list of songs in the dataset.

### `GET /songs/{spotify_id}`

Get the given song's 20 most similar songs.

### `POST /songs/recommendation`

Get a list of recommendations by submitting a dictionary with Spotify IDs as the key and 1 for like or -1 for dislike as the value. For example (minus the comments):

```python
{
  # Bad Romance - Lady Gaga
  "5P5cGNzqh6A353N3ShDK6Y": 1,

  # Woman, Amen - Dierks Bentley
  "4YX7OBp0yoMwC6eZNNg5ky": -1,

  # Cold Wind Blows - Eminem
  "3Tj1luJyKPQt7WbrqpJ2Az": 1,

  # Auld Lang Syne - Kenny G
  "7h4FywzqhgZrrvpiLDJ2vw": -1,

  # Cyanide - Metallica
  "2LfonCFEOzFedikP12rTeo": 1
}
```
