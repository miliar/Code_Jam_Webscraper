#!/usr/bin/python3
__author__ = 'Tianren Liu'

import sys
import numpy as np

if __name__ == "__main__":
    _T = int(sys.stdin.readline())
    for _t in range(1,_T+1):
        N,P = map(int, sys.stdin.readline().split())

        G = list(map(int, sys.stdin.readline().split()))
        C = [0] * P;
        for i in G:
            C[i % P] += 1
        s = sum((i*C[i] for i in range(P))) % P
        if s != 0:
            C[P - s] += 1

        T = C[0]
        C[0] = 0

        if P == 2:
            T += C[1] // 2
            # C[1] = 0
        elif P == 3:
            m = min(C[1], C[2])
            T += m + (C[1]-m)//3 + (C[2]-m)//3
            # C[1] = C[2] = 0
        elif P == 4:
            m = min(C[1], C[3])
            T += m
            C[1] -= m
            C[3] -= m
            C[2] += (C[1] + C[3]) // 2
            T += C[2] // 2

        print("Case #{}: {}".format(_t, T))
