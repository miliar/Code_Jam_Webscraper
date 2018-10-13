#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

C = int(sys.stdin.readline())
for c in range(1,C+1):
    r, t = map(int, sys.stdin.readline().split())
    res = 0
    while t > 0:
        paint = ((r+1)**2) - (r**2)
        if paint <= t:
            res+=1
            t-=paint
            r +=2
        else:
            break
    print "Case #%d: %d" % (c , res)
