#!/usr/bin/python3
__author__ = 'Tianren Liu'

import sys
import numpy as np
import math

def kitnum(N,P,R,Q):
    kits = 0

    while min([len(q) for q in Q]) > 0:
        cand = [q.pop() for q in Q]
        while min(c[0] for c in cand) < max(c[1] for c in cand):
            up = min(c[0] for c in cand)
            for i in range(N):
                if cand[i][1] > up:
                    if len(Q[i]) > 0:
                        cand[i] = Q[i].pop()
                    else:
                        return kits

        kits += 1 #min(c[0] for c in cand)
    return kits

if __name__ == "__main__":
    __T = int(sys.stdin.readline())
    for __t in range(1,__T+1):
        N,P = list(map(int,sys.stdin.readline().split()))
        R = list(map(int,sys.stdin.readline().split()))
        Q = [[(math.floor(r/(0.9*R[i])), math.ceil(r/(1.1*R[i])))
            for r in sorted(map(int,sys.stdin.readline().split()))
            if math.floor(r/(0.9*R[i])) >= math.ceil(r/(1.1*R[i]))]
            for i in range(N)]

        print("Case #{}: {}".format(__t, kitnum(N,P,R,Q)))
