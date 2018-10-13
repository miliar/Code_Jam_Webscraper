#!/bin/python

import sys
import math

inf = sys.stdin
T = int(inf.readline())
    
for t in range(T):
    L, P, C = map(int, inf.readline().split())
    choices = []
    while L < P:
        L *= C
        choices.append(L)
    
    y = math.ceil(math.log(len(choices), 2))
    print 'Case #%d: %d' % (t+1, y)
