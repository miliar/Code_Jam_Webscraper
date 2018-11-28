#!/usr/bin/env python

from sys import stdin
from operator import xor

T = int(stdin.readline())

for CASO in xrange(1,T+1):
    N = int(stdin.readline())
    C = [int(x) for x in stdin.readline().strip().split(" ")]

    C.sort()
    found = False

    for i in xrange(1,N):
        left, right = C[:i], C[i:]

        if reduce(xor, left) == reduce(xor, right):
            found = True
            print "Case #%d: %d" % (CASO, sum(right))
            break

    if not found:
        print "Case #%d: NO" % (CASO)
