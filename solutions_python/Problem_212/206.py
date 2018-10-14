#!/usr/bin/env python

from sys import stdin, stderr
from math import ceil, floor
from numpy import array

T = int(stdin.readline())

def Solve(G, P):
    if P == 2:
        ret  = sum(G % 2 == 0)
        ret += (len(G) - ret + 1) / 2
    elif P == 3:
        G0 = sum(G % 3 == 0)
        G1 = sum(G % 3 == 1)
        G2 = sum(G % 3 == 2)
        ret  = G0
        ret += min([G1, G2])
        ret += (abs(G1 - G2) + 2) / 3
    elif P == 4:
        G0 = sum(G % 4 == 0)
        G1 = sum(G % 4 == 1)
        G2 = sum(G % 4 == 2)
        G3 = sum(G % 4 == 3)
        ret  = G0
        ret += G2 / 2
        G2 %= 2
        ret += min([G1, G3])
        G1 = abs(G1 - G3)
        ret += (G1 + G2 * 2 + 3) / 4
    print ret
    pass

# for i in range(100):
#     print Solve('A' * 1000)
# exit(0)


for t in range(T):
    N, P = tuple([int(v) for v in stdin.readline().split()])
    G = array([int(v) for v in stdin.readline().split()])

    print "Case #%d:" % (t+1),
    Solve(G, P)
