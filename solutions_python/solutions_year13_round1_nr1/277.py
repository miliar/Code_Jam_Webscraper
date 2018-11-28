#! /usr/bin/env python

from decimal import *
from math import sqrt

getcontext().prec = 50

T = int(raw_input())

for case in xrange(T):
    r, t = map(int, raw_input().split())
    ans = 4 * r * r - 4 * r + 8 * t + 1
    ans = Decimal(ans).sqrt()
    ans -= 2 * r + 3
    print "Case #%d: %s" % (case + 1, int(ans) / 4 + 1)
