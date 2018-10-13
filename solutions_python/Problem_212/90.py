#!/opt/local/bin/python

from collections import Counter
"""Premature optimization is the root of all evil."""

import sys
import re

def doit(N, P, G):
    G = ([x % P for x in G])
    C = Counter(G)
    t = C[0]

    #print(C)
    C[0] = 0

    for x in range(1,P//2+1):
        #print(str(x) + ': ')
        m = min(C[x], C[P-x])
        C[x] -= m
        C[P-x] -= m
        t += m
    if P % 2 ==  0:
        m = C[P//2]//2
        C[P//2] -= m
        C[P//2] -= m
        t += m

    if P == 3:
        for i in (1,2):
            d = C[i] // 3
            t += d
            C[i] -= d * 3
    if P == 4:
        b = [x % 3 for x in (C[1], C[3])]
        

    if any(y for x, y in C.items()):
        #print(C)
        t += 1

    return t

T = int(sys.stdin.readline())
for casenum in range(T):
    (N, P) = sys.stdin.readline().split()
    G = sys.stdin.readline().split()

    n = doit(int(N), int( P), [int(a) for a in G])




    print("Case #" + str(casenum + 1) + ": " + str(n))
