#!/usr/bin/env python
# -*- coding: utf-8 -*-
T = int(raw_input())

for i in xrange(1,T+1):
    C,F,X = map(float,raw_input().split(" "))

    if X==0:
        ans = 0
    if C>=X:
        ans = X/2

    r = 2 # rate
    t = 0 # time

    while True:
        if (X/r <= ((C/r) + (X/(r+F)))):
            ans = t + X/r
            break
        t += C/r
        r += F

    print "Case #%d: %.7f" % (i,ans)
