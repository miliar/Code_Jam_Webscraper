#!/usr/bin/env python

from sys import stdin

t = input()

for test in range(t):
    n = input()
    perm = [int(i)-1 for i in stdin.readline().strip().split()]
    
    tot = 0
    for i in xrange(n):
        if perm[i] != i:
            tot += 1
    
    print "Case #%d: %d.000000" % (test+1, tot)