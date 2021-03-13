def cosine_similarity(X, Y): 
    x_norm = (X ** 2).sum() ** (1/2)
    y_norm = ((Y ** 2).sum(axis=1) ** (1/2))
    return (X @ Y.T) / (x_norm * y_norm)

def jaccards_coefficient(X, Y):
    dot_product = (X @ Y.T)
    return dot_product / ((X ** 2).sum() + (Y ** 2).sum(axis=1) - dot_product)