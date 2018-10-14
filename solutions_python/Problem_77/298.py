#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, math

rl = lambda: sys.stdin.readline().strip()
cases = int(rl())
for cc in xrange(cases):
    n = int(rl())
    array = map(int,rl().split())
    in_place = 0
    for i in xrange(n):
        if i+1 == array[i]:
            in_place += 1
    print "Case #%d: %.10lf" % (cc+1, float(n - in_place))
