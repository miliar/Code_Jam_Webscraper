#!/usr/bin/env python
# Python 2.6.6

import operator

t = int(raw_input())

for i in xrange(1, t+1):
    n = int(raw_input())
    xs = map(int, raw_input().split())
    v = reduce(operator.xor, xs)
    print("Case #%d: %s" % (i, str(sum(xs) - min(xs)) if v == 0 else "NO"))
