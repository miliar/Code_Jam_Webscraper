#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

fin = open('candy.in','r')
T = int(fin.readline())
for t in range(T):
    N = [int(i) for i in fin.readline().split()][0]
    data = [int(i) for i in fin.readline().split()]
    a=0
    for i in range(N):
        a = a^data[i]
    if a == 0:
        print "Case #"+str(t+1)+": "+str(sum(data)-min(data))
    else:
        print "Case #"+str(t+1)+": NO"
