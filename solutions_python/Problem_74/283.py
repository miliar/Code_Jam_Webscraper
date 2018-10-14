#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

fin = open('bot.in','r')
T = int(fin.readline())
for t in range(T):
    data = [i for i in fin.readline().split()][1:]
    time = [0,0]
    pos = [1,1]
    alltime = 0
    for i in range(len(data)/2):
        j = 0 if data[2*i]=="B" else 1;
        q = max(0,abs(pos[j]-int(data[2*i+1]))-time[j])+1
        pos[j] = int(data[2*i+1])
        time[j] = 0
        time[1-j] += q
        alltime += q
    print "Case #"+str(t+1)+": "+str(alltime)
