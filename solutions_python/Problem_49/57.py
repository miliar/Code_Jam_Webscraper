#!/usr/bin/python
"Google Round2 - D"

import sys
import re
from mpmath import *
mp.dps = 50

def permutations(L):
    if len(L) <= 1:
        yield L
    else:
        a = [L.pop(0)]
        for p in permutations(L):
            for i in range(len(p)+1):
                yield p[:i] + a + p[i:]

def sprinker(p1, p2):
    global plants
    (x1, y1, r1) = plants[p1]
    (x2, y2, r2) = plants[p2]
    d = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) + r1 + r2
    return d / 2.0

cases = int(raw_input())

for case in range(1, cases + 1):
    N = int(raw_input())
    plants = {}
    for p in range(0, N):
        line = raw_input().strip().split()
        X = int(line.pop(0))
        Y = int(line.pop(0))
        R = int(line.pop(0))
        plants[p] = (X, Y, R)

    c = 10000
    for choice in permutations(range(0, N)):
        #print repr(choice)
        if N >= 3:
            cr = max(sprinker(choice[0], choice[1]), sprinker(choice[2], choice[2]))
        elif N == 2:
            cr = max(sprinker(choice[0], choice[0]), sprinker(choice[1], choice[1]))
        else:
            cr = sprinker(choice[0], choice[0])
        if cr < c:
            c = cr

    print 'Case #%s: %0.6f' % (case, c)
