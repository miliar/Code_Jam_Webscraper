#!/usr/bin/python3
__author__ = 'Tianren Liu'

import sys
import numpy as np

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        S,K = sys.stdin.readline().split()
        K = int(K)
        S = list(s=='+' for s in S)
        M = 0
        for i in range(len(S) - K + 1):
            if not S[i]:
                for j in range(i,i+K):
                    S[j] = not S[j]
                M = M + 1
        Succ = True
        for s in S:
            Succ = Succ and s
        if Succ:
            print("Case #{}: {}".format(t,M))
        else:
            print("Case #{}: IMPOSSIBLE".format(t))
