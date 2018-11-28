#!/usr/bin/env python3
import sys
from math import pi
from decimal import *


def rri():
    return map(int, input().split())

T = int(input())
for i in range(T):
    N, K = rri()
    R = [0 for _ in range(N)]
    H = [0 for _ in range(N)]
    ri = [iii for iii in range(N)]
    hi = [iii for iii in range(N)]
    for j in range(N):
        r, h = rri()
        R[j] = r
        H[j] = h
    ri.sort(key=lambda e: R[e])
    ans = -1000
    for j in range(N):
        ii = []
        pos = ri.index(j)
        if pos < K-1:
            continue
        for k in range(pos):
            ii.append(ri[k])
        ii.sort(key=lambda e: -2*pi*R[e]*H[e])
        ss = 2*pi*R[j]*H[j] + pi*R[j]**2
        for k in range(K-1):
            ss += 2*pi*R[ii[k]]*H[ii[k]]
        ans = max(ans, ss)
    print("Case #%d:"%(i+1), ans)
