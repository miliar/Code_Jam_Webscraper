#!/usr/bin/env python

import sys
line = sys.stdin.readline()
data = [map(int, line.split()) for line in sys.stdin.readlines()]

from fractions import gcd

i=0
for j in data:
    del j[0]
    j.sort()
    j.reverse()
    i += 1
    k = reduce(gcd, map(lambda (p,q) : (p-q), zip(j,j[1:])))
    j = j[-1]
    a, b = divmod(j, k)
    if b:
        a += 1
    c = a * k - j
    print 'Case #%i: %i' % (i, c)
