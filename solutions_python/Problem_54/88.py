#!/usr/bin/python

import sys
import fractions

C = int(sys.stdin.readline())

for c in range(C):
    list = sys.stdin.readline().split()
    N = int(list[0])
    t = map(int, list[1:])
    t.sort()
    ts = map(lambda x,y : x - y, t[1:], t[:-1])
    g = reduce(fractions.gcd, ts)
    if t[0]%g == 0:
        mt = 0
    else:
        mt = g - t[0]%g;
    print 'Case #%d: %d'%(c+1, mt)

    



