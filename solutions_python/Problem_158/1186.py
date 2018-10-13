#!/usr/bin/env python

import sys

def run(data):
    x, R, C = data
    l = max(R, C)
    s = min(R, C)
    if (x > 6 or
        l * s % x or
        s < (x + 1) / 2 or
        s < x and l < x):
        return True

    if s >= x:
        return False

    if s > 1 and not x % s:
        return True

    return False

lines = open(sys.argv[1]).readlines()

test_set = []
T = int(lines.pop(0))
for i in xrange(T):
    data = [int(s) for s in lines.pop(0).split()]
    print 'Case #%s: %s' % (i+1, 'RICHARD' if run(data) else 'GABRIEL')
