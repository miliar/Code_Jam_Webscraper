#!/usr/bin/env python
# Python 2.6.5

from math import log, ceil

t = int(raw_input())

for tc in xrange(1, t+1):
    l, p, c = map(int, raw_input().split())
    i, _l = 0, l
    while _l < p:
        i += 1
        _l *= c
    print("Case #%d: %d" % (tc, ceil(log(i, 2))))
