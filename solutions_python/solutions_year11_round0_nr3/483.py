#!/usr/bin/python
import functools
import operator

t = int(raw_input())

for i in xrange(t):
    n = int(raw_input())
    c = map(int, raw_input().split())
    if functools.reduce(operator.xor, c) != 0:
        print "Case #%d: NO" % (i+1)
    else:
        s = sum(sorted(c)[1:])
        print "Case #%d: %d" % (i+1, s)
