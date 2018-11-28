#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import mul
from itertools import product

def substitute(n, control):
    if control == 'x':
        return 1-n
    else:
        return n

def solve(a, b, p):
    expected = []
    # RA
    expected.append(b+2)
    # KT
    pp = reduce(mul, p)
    kt = pp * (b-a+1) + (1-pp) * (2*b - a + 2)
    expected.append(kt)
    for i in xrange(1,a+1):
        try:
            pp = reduce(mul, p[:-i])
        except:
            pp = 0
        expected.append(pp * (b-a+2*i+1) + (1-pp) * (2*b-a+2*i+2))
    return min(expected)

t = int(raw_input())

for i in xrange(t):
    a,b = [int(j) for j in raw_input().strip().split(" ")]
    p = [float(j) for j in raw_input().strip().split(" ")]
    out = solve(a, b, p)
    print "Case #{0}: {1}".format(i+1, out)
