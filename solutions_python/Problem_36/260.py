#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

fin = open('welcomet.in','r')
N = int(fin.readline()[:-1])
wel = "welcome to code jam"
l = len(wel)
for n in range(N):
    p = [0]*l
    p[0:0] = [1]
    for c in fin.readline()[:-1]:
        for i in range(l):
            if c == wel[i]:
                p[i+1]=(p[i+1]+p[i])%1000
    print "Case #"+str(n+1)+": "+str(p[l]).zfill(4)
