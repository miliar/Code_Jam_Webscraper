#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 12:04:51 2017

@author: lyj
"""

T = int(raw_input())
for horse in xrange(T):
    s = raw_input().split()
    dist = int(s[0])
    numh = int(s[1])
    data = []
    for i in xrange(numh):
        di = raw_input().split()
        ini = int(di[0])
        spi = int(di[1])
        data.append([ini, spi])
    data.sort()
    tmax = (dist-data[-1][0])*1.0/data[-1][1]
    for i in xrange(numh - 1, -1, -1):
        temp = (dist-data[i][0])*1.0/data[i][1]
        if temp > tmax:
            tmax = temp
    speed = dist*1.0/tmax
    print "Case #" + str(horse+1) + ":", speed