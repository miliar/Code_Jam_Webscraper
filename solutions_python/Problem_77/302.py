#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

fin = open('goro.in','r')
T = int(fin.readline())
for t in range(T):
    N = [int(i) for i in fin.readline().split()][0]
    data = [int(i)-1 for i in fin.readline().split()]
    seen = [False for i in range(N)]
    circles = []
    for i in range(N):
        if seen[i]:
            continue
        q = data[i]
        seen[q] = True
        c = 1
        while q != i:
            q = data[q]
            seen[q] = True
            c += 1
        circles.append(c)
    print "Case #"+str(t+1)+": "+str(sum([(c if c>=2 else 0) for c in circles]))
