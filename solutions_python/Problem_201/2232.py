import numpy as np
from numba import njit

@njit
def split(x):
    # split x to two parts
    x2 = x // 2
    if (x % 2) != 0:
        return x2, x2
    else:
        return x2, x2 - 1

@njit
def iterate(X):    
    maxx, maxind = X[:, 0].max(), X[:, 0].argmax()

    for x in split(maxx):
        bool_ind = X[:, 0] == x
        if bool_ind.sum() > 0:
            X[bool_ind, 1] += 1
        else:
            X = np.concatenate((X, np.atleast_2d(np.array([x, 1]))))
            
    if X[maxind, 1] > 1:
        X[maxind, 1] -= 1
    else:
        X = np.concatenate((X[:maxind], X[(maxind + 1):]))
    return X

@njit
def main(N, K):
    X = np.atleast_2d(np.array([N, 1]))
    for i in range(K - 1):
        X = iterate(X)
    return split(X[:, 0].max())

T = int(input()) 
for i in range(1, T + 1):
  N, K = [int(s) for s in input().split(' ')]
  maxi, mini = main(N, K)
  print("Case #{}: {} {}".format(i, maxi, mini))