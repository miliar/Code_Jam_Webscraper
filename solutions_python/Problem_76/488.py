#!/usr/bin/env python
import os
import sys

t = int(sys.stdin.readline())
for test in range(t):
    n = int(sys.stdin.readline())
    c = [int(x) for x in sys.stdin.readline().split()]
    p = 0
    for i in c:
        p = p ^ i

    c.sort()

    if p > 0:
        print "Case #%d: %s" % (test+1,"NO") 
    else:
        print "Case #%d: %s" % (test+1,sum(c[1:])) 
