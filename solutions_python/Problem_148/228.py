#!/usr/bin/env python

import sys
from collections import defaultdict

def Solve(X, sizes):
    half = X / 2
    remainder = []
    free = []

    sizes = sorted(sizes, reverse=True)
    #print X, sizes

    border = 0
    for s in sizes:
        if s > half: 
            border += 1
            remainder.append(X - s)
        else: break

    free = sorted(sizes[border:])
    remainder = sorted(remainder)

    i, j = 0, 0
    paired = 0
    while(True):
        if j == len(remainder) or i == len(free): break
        if free[i] > remainder[j]: 
            j += 1
        else:
            i += 1
            j += 1
            paired += 1

    badleft = len(remainder) - paired
    left = len(free) - i
    return str(paired + badleft + left / 2 + left % 2)
    

inp = open(sys.argv[1], 'r').readlines()
T = int(inp[0].strip())
for t in range(T):
    N, X = map(int, inp[2*t+1].strip().split())
    sizes = map(int, inp[2*t+2].strip().split())
    print "Case #"+str(t+1)+": "+Solve(X, sizes)

    
