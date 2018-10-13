#!/opt/local/bin/python

from math import ceil

"""Premature optimization is the root of all evil."""

import sys
import re

dbg = False
dbg = 4
dbg = False
dbg = 4
dbg = 4

dbg = False
def doit(N, C,M,T,P,B):
    req = [sum([x[i] for x in T]) for i in range(N)]

    if dbg:
        print('0'*80)
        print(str(N) + ' ' + str(C) + ' ' + str(M))
        print(T)
        print('.'*40)
        print(req)

    M = max([sum(x) for x in T])

    if dbg:
        print(M)

    sigma = 0
    for i in range(N):
        sigma += req[i]
        M = max(M, ceil(sigma / (i+1)))

    # In theory M rides suffice?
    proms = 0
    for i in req:
        proms += max(i-M, 0)

    return (M, proms)


T = int(sys.stdin.readline())
for casenum in range(T):
    # data = sys.stdin.readline().split()
    (N, C, M) = [int(x) for x in sys.stdin.readline().split()]
    P = []
    B = []
    T = [[0 for _ in range(N)] for _ in range(C)]
    for _ in range(M):
        (x,y)  = [int(x) for x in sys.stdin.readline().split()]
        x -= 1
        y -= 1
        P.append(x)
        B.append(y)
        T[y][x] += 1

    n = doit(N,C,M,T,P,B)




    print("Case #" + str(casenum + 1) + ": " + " ".join([str(x) for x in n]) )
