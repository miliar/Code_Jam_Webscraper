#! /usr/bin/env python
#coding=utf-8

import sys

f = open(sys.argv[1]).read().splitlines()
for t in xrange(int(f[0])):
    u = t + 1
    mins, maxs = f[u].split()
    min = int(mins)
    max = int(maxs)
    lst = {}
    n = len(mins)
    exp = 10 ** (n - 1)
    for i in xrange(min, max + 1):
        p = i
        for j in xrange(n-1):
            p = p / 10 + (p % 10) * exp
            if p > i and p <= max:
                lst[(i, p)] = 1
    print 'Case #%d: %d' % (u, len(lst))