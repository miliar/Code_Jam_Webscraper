#!/usr/bin/python
import sys

memo = {}


T = int(sys.stdin.readline())
for i in xrange(T):
    print "Case #%d:" % (i+1),
    c, f, x = map(float, sys.stdin.readline().split(" "))
    t = 0.0
    best = float('inf')
    r = 2.0
    while True:
        if t + x/r > best:
            print best
            break
        else:
            best = t + x/r
            t += c/r
            r += f
