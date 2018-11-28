#!/usr/bin/env python

import sys


cnt = int(sys.stdin.readline())

for ii in range(cnt):
    print >>sys.stderr, "solving %d" % ii
    i_from, i_to = map(int, sys.stdin.readline().strip().split())

    result = 0
    done = set()

    for x in range(i_from, i_to + 1):
        xs = str(x)
        for i in range(len(xs)):
            xs = xs[1:] + xs[0]
            xx = int(xs)
            if x < xx and xx >= i_from and xx <=i_to:
                done.add((x, xx))
       
    
    print "Case #%d: %d" % (ii + 1, len(done),)

