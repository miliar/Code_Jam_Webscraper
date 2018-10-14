#!/usr/bin/env python3
import math

T = int(input())

for t in range(1, T+1):
    D = int(input())
    P = [int(x) for x in input().split()]
    P.sort()
    P.reverse()

    opt = max(P)

    for gr in range(1, opt):
        kroki = 0
        for p in P:
            if p <= gr:
                break
            kroki += math.ceil((p - gr) / gr)
        if kroki + gr < opt:
            opt = kroki + gr

    print("Case #{}: {}".format(t, opt))

