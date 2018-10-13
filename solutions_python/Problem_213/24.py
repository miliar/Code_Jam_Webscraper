#!/usr/bin/python3
__author__ = 'Tianren Liu'

import sys
import numpy as np

if __name__ == "__main__":
    _T = int(sys.stdin.readline())
    for _t in range(1,_T+1):
        N,C,M = map(int, sys.stdin.readline().split())

        Cperson = [0] * C
        Cseat = [0] * N
        for _ in range(M):
            Pi, Bi = map(int, sys.stdin.readline().split())
            Cperson[Bi-1] += 1
            Cseat[Pi-1] += 1

        R = max(Cperson)
        s = 0
        for i in range(N):
            s += Cseat[i]
            R = max(R, (s+i) // (i+1))
        promo = sum((max(z-R,0) for z in Cseat))

        print("Case #{}: {} {}".format(_t, R, promo))
