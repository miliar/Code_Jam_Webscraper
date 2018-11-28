#!/usr/bin/env python

from sys import stdin

t = input()

for test in range(t):
    n = input()
    candies = [int(i) for i in stdin.readline().strip().split()]
    
    if reduce(lambda a, b: a^b, candies) == 0:
        print "Case #%d: %d" % (test+1, sum(candies) - min(candies))
    else:
        print "Case #%d: NO" % (test+1)