#!/usr/bin/env python3

import sys, os, re
import numpy as np
import math
from collections import defaultdict

def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    T = int(input().strip())
    for t in range(1, T+1):
        D, N = [int(x) for x in input().strip().split(" ")]
        #K = [0 for x in range(N)]
        #S = [0 for x in range(N)]
        K = np.zeros((N,), dtype=np.float64)
        S = np.zeros((N,), dtype=np.float64)
        for i in range(N):
            K[i], S[i] = [int(x) for x in input().strip().split(" ")]
            
        #log("K: ", K)
        #log("S: ", S)
        #b = [['.' for i in range(N)] for j in range(N)]

        T = np.zeros((N,), dtype=np.float64)
        for i in range(N):
            T[i] = (D-K[i])/S[i]

        ans = D/np.max(T)
        print("Case #{}: {}".format(t, ans))

if __name__ == '__main__':
    main()
