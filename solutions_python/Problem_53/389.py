#!/usr/bin/env python

from sys import stdin

t = int(stdin.readline())
for case in xrange(t):
    n, k = [int(x) for x in stdin.readline().split()]
    mask = pow(2, n) - 1
    result = 'OFF'
    if k & mask ^ mask == 0:
        result = 'ON'
    print 'Case #%i: %s' % (case + 1, result)
