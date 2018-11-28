#!/usr/bin/env python

from math import log


for nnn in xrange(1, int(raw_input())+1):
    print "Case #%d:" % (nnn),
    N, K = [int(x) for x in raw_input().split()]
    if K == 1:
        print N/2, (N-1)/2
        continue
    depth = int(log(K, 2))
    x = 2**depth
    leaves = K - x + 1
    z = (N-x+1) / x
    surplus = N - x + 1 - z*x
    if leaves <= surplus:
        z += 1
    print z/2, (z-1)/2

