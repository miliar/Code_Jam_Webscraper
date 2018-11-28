#!/usr/bin/python3
__author__ = 'Tianren Liu'

import sys
import numpy as np
import math

inf = np.inf

def solve():
    N, Q = map(int, sys.stdin.readline().split())
    ES = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    E = [e for e,s in ES]
    S = [s for e,s in ES]
    _D = [[d if d>=0 else inf for d in map(int, sys.stdin.readline().split())] for _ in range(N)]

    _UV = [list(map(int, sys.stdin.readline().split())) for _ in range(Q)]
    UV = [(u-1,v-1) for u,v in _UV]

    D = np.array(_D)
    for i in range(N):
        D[i,i] = 0
    for _ in range(10):
        for i in range(N):
            for j in range(N):
                D[i,j] = min((D[i,k]+D[k,j] for k in range(N)))


    Dt = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            if D[i,j] > E[i]:
                Dt[i,j] = inf
            else:
                Dt[i,j] = D[i,j]/S[i]
    for _ in range(10):
        for i in range(N):
            for j in range(N):
                Dt[i,j] = min((Dt[i,k]+Dt[k,j] for k in range(N)))

    res = [Dt[u,v] for u,v in UV]

    return "{}".format(' '.join(map(str,res)))

if __name__ == "__main__":
    __T = int(sys.stdin.readline())
    for __t in range(1,__T+1):
        print("Case #{}: {}".format(__t, solve()))
