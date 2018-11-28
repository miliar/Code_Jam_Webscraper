#!/usr/bin/env python

from sys import stdin, stderr
from math import ceil, floor

T = int(stdin.readline())

def Solve(R, C, cake):
    first_line = True
    for i in range(R):
        hit = False
        for j in range(C):
            if cake[i][j] != '?':
                hit = True
                break
            pass
        if not hit:
            if not first_line: cake[i] = cake[i-1]
            continue
        newrow = cake[i][j] * j
        char = cake[i][j]
        for jj in range(j, C):
            if cake[i][jj] != '?': char = cake[i][jj]
            newrow += char
            pass
        cake[i] = newrow
        if first_line:
            for ii in range(i): cake[ii] = cake[i]
            first_line = False
            pass
        pass
    for c in cake: print c

# for i in range(100):
#     print Solve('A' * 1000)
# exit(0)


for t in range(T):
    R, C = tuple([int(v) for v in stdin.readline().split()])
    cake = []
    for i in range(R): cake.append(stdin.readline().strip())

    print "Case #%d:" % (t+1)
    Solve(R, C, cake)
