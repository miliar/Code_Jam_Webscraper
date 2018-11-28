#!/usr/bin/python

import sys
from math import *
from fractions import *

C = int(sys.stdin.readline())

for i in range(C):
    line = sys.stdin.readline().strip().split()
    N = int(line[0])

    t = []
    for j in range(N):
        t.append(long(line[j+1]))
    t.sort()
    #print t
    smallest = t[0]
    for j in range(N):
        t[j] = t[j] - smallest

    M = t[1]

    for j in range(1,N):
        M = gcd(M,t[j])
    
    #print "M=",M

    forceil = 0
    if smallest % M != 0:
        forceil = 1
    result = ((smallest / M) + forceil) * M - smallest
    print "Case #%d: %d" % (i+1,result)
