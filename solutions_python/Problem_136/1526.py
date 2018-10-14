#!/usr/bin/python

import math

def solve(C, F, X):
    N = int(math.floor((X*F-2.0*C)/(C*F)))
    if N<0:
        N = 0
    s = X/(2.0+N*F)
    for i in range(N):
        s += C/(2.0 + (N-1-i)*F)
    return s

def readFloats(): return [float(i) for i in raw_input().split()]

for test in range(int(raw_input())):
    C,F,X = readFloats()

    print 'Case #%d:' % (test+1), solve(C, F, X)
