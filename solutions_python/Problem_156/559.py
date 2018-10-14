#!/usr/bin/env python

import sys

ls = sys.stdin.readlines()
n = int(ls[0])
nc = 1
for i in xrange(n):
    d = int(ls[1 + i*2])
    ds = [int(x) for x in ls[2 + i*2].split()]
    ds = ds[:d]
    
    m = max(ds)
    b = m
    for j in xrange(1, m):
        b = min(b, sum(max(0, (x + j - 1) / j - 1) for x in ds) + j)
    print "Case #%d: %d" % (nc, b)
    nc += 1
