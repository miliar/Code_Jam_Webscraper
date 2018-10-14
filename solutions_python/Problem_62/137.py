#!/usr/bin/env python

from itertools import count, izip
import sys

T = int(sys.stdin.readline())

for i in xrange(1, T + 1):
    N = int(sys.stdin.readline())
    wires = []
    result = 0
    for j in xrange(N):
        w = tuple(int(x) for x in sys.stdin.readline().split())
        for x in wires:
            if (w[0] < x[0] and w[1] > x[1]) or (w[0] > x[0] and w[1] < x[1]):
                result += 1
        wires.append(w)

    print 'Case #%i: %s' % (i, result)
