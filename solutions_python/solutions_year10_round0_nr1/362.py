#!/usr/bin/env python
# http://code.google.com/codejam/contest/dashboard?c=433101#s=p0

from sys import stdin
from draft import snap

# Testcases
T = int(stdin.readline())
for t in range(T):
    N, K = map(int, stdin.readline().split())
    on = K % 2**N == 2**N-1
    print "Case #%d: %s" % (t + 1, 'ON' if on else 'OFF')
