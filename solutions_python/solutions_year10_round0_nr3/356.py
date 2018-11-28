#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import math

t = int(sys.stdin.readline())

for case in range(t):
    [r, k, n] = [int(i) for i in sys.stdin.readline().split()]
    q = [[-1,-1,int(i)] for i in sys.stdin.readline().split()]
    sum = 0
    looplen = 0
    sumlen = 0
    for roll in range(r):
        ## 
        if q[0][0] > 0: 
            looplen = roll - q[0][0]
            sumlen = sum - q[0][1]
            break
        else:
            q[0][0] = roll
            q[0][1] = sum
        num = 0
        for c,j in enumerate(q):
            if num+j[-1] >k:
                break
            num += j[-1]
        sum += num
        q = q[c:] + q[0:c]

    if sumlen and looplen:
        sum += sumlen * ((r-roll)/looplen)
        for i in range((r-roll)%looplen):
            num = 0
            for c,j in enumerate(q):
                if num+j[-1] >k:
                    break
                num += j[-1]
            sum += num
            q = q[c:] + q[0:c]

    print "Case #%d: %d"%(case+1, sum)
