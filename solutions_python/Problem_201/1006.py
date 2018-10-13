#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:56:46 2017

@author: tianxia
"""
import heapq
f = open("3.small.2.in.txt")
w = open("3.small.2.out.txt", "w")
t = int(f.readline())
for ti in range(1, t+1):
    n, k = map(int, f.readline().strip().split())
    h = [-n]
    y = 0
    z = 0
    for i in range(k):
        space = -heapq.heappop(h) - 1
        z = space//2
        if space % 2==0:
            y = space//2
        else:
            y = space//2 + 1
        heapq.heappush(h, -y)
        heapq.heappush(h, -z)
    
    w.write("Case #%d: %d %d\n" % (ti, y, z))
w.close()