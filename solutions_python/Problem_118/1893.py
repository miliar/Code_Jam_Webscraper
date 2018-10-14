#!/usr/bin/env python

import sys

from math import sqrt

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    count = 0
    for x in xrange(a, b+1):
        sx = str(x)
        if sx == sx[::-1]:
            y = int(sqrt(x))
            if y * y == x:
                sy = str(y)
                if sy == sy[::-1]:
                    count += 1
    print "Case #%d: %d" % (i+1, count)