#!/usr/bin/env python
from sys import stdin

tn = int(stdin.readline())
for ti in xrange(tn):
	d, n = map(int, stdin.readline().split())
        t = 0
        for i in xrange(n):
            k, s = map(int, stdin.readline().split())
            t = max(t, float(d-k)/s)
        print 'Case #{}: {:.6f}'.format(ti+1, d / t)
