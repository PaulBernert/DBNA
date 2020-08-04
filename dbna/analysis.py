import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AffinityPropagation, KMeans

def parse(filename, selection):
    df = pd.read_csv(filename)
    locations = [", ".join((i,j)) for i,j in df[['State','City']].values]
    data = df[df.columns[selection].values].values
    for i in range(data.shape[1]):
        column = data[:,i]
        if np.isnan(column).any():
            column[np.isnan(column)] = column[[not i for i in np.isnan(column)]].mean()
            data[:,i] = column[:]
    return locations, data

def distance(A, B, W=None):
    assert A.shape == B.shape
    if W is None:
        W = np.array([1 for _ in range(A.shape[0])])
    W = np.array(W)
    return np.sqrt(np.sum(W*(A-B)**2))

def distance_matrix(data, W=None):
    dist_matrix = np.zeros((data.shape[0], data.shape[0]))
    if W is None:
        W = 1 / data.max(axis=0)
    for i in range(dist_matrix.shape[0]):
        for j in range(dist_matrix.shape[1]):
            A = data[i]
            B = data[j]
            dist_matrix[i,j] = distance(A, B, W)
    return dist_matrix

def transform(clusters, locations):
    nlabels = []
    nclusters = []
    for i in np.unique(clusters.labels_):
        expansion = np.array(locations)[clusters.labels_ == i]
        for j in expansion:
            nclusters.append(i)
            nlabels.append(j)
    return nlabels, nclusters

def clustering_ap(distance_matrix, locations):
    clusters = AffinityPropagation(affinity='precomputed')
    clusters.fit(-distance_matrix)
    return transform(clusters, locations)

def clustering_kmeans(distance_matrix, locations, n_clusters=10):
    clusters = KMeans(n_clusters=n_clusters)
    clusters.fit(distance_matrix)
    return transform(clusters, locations)

def plot_sorted(labels, clusters):
    fig, ax = plt.subplots(1, figsize=(20,5))
    ax.stem(np.array([i for i in range(len(labels))]), clusters, '.', use_line_collection=True)
    ax.set_xticks([i for i in range(len(labels))])
    ax.set_xticklabels(labels, rotation=90)
    return ax
    
def plot_matrix(labels, distance_matrix):
    fig, ax = plt.subplots(1, figsize=(20,20))
    im = ax.imshow(distance_matrix)
    ax.set_xticks([i for i in range(len(labels))])
    ax.set_xticklabels(labels, rotation=90)
    ax.set_yticks([i for i in range(len(labels))])
    ax.set_yticklabels(labels, rotation=0)
    fig.colorbar(im,ax=ax)
    return ax
