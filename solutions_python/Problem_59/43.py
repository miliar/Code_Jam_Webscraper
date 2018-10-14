#!/usr/bin/env python

from sys import stdin, exit
from math import fabs

T = int(stdin.readline())

for CASO in xrange(1,T+1):
    (N, M) = [int(x) for x in stdin.readline().split(" ")]

    existing = []
    new = 0

    for i in xrange(N):
        dir = stdin.readline().strip().split("/")[1:]
        existing.append(dir)

    for i in xrange(M):
        dir = stdin.readline().strip().split("/")[1:]

        for end in xrange(1,len(dir)+1):
            if dir[:end] not in existing:
                new += 1
                existing.append(dir[:end])

    print "Case #%d: %d" % (CASO, new)
