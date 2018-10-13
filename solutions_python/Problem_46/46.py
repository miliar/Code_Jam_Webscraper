#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

fin = open('crazyt.in','r')
T = int(fin.readline()[:-1])
for t in range(T):
    N = int(fin.readline()[:-1])
    m = []
    for i in range(N):
        m.append(max(0,fin.readline().rfind('1')))
    K = 0
    for j in range(N):
        if m[j] > j:
            s = j
            while m[s] > j:
                s+=1
                K+=1
            m = m[0:j] + [m[s]] +m[j:s]+m[s+1:]
    print "Case #"+str(t+1)+": "+str(K)
