#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

def average(l):
    return sum(l, 0.0) / len(l)

fin = open('rpi.in','r')
T = int(fin.readline())
for t in range(T):
    print "Case #"+str(t+1)+":"
    N = int(fin.readline())
    data = []
    for i in range(N):
        data.append(fin.readline())
    
    WP = [float(sum(1 for x in data[i] if x == '1'))/sum(1 for x in data[i] if x in ['1','0']) for i in range(N)]
    OWP = [ average([float(sum(1 for x in data[j] if x == '1')-(1 if data[j][i]=='1' else 0))/(sum(1 for x in data[j] if x in ['1','0'])-1) \
            for j in range(N) if data[i][j] != '.']) for i in range(N)]
    OOWP = [ average([OWP[j] for j in range(N) if data[i][j]!='.']) for i in range(N) ]
    for i in range(N):
       print 0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]
fin.close()
