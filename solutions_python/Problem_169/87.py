# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:45:21 2015

@author: guy
"""
#from __future__ import print_function, division, input
import numpy as np


def simple(sources,n,v,x):
    if n == 1:
        if abs(x-sources[0][1]) < 1e-8:
            return v/sources[0][0]
        else:
            return "IMPOSSIBLE"
    elif n == 2:
        if x+1e-8 < min(sources[i][1] for i in range(2)) or x-1e-8 > max(sources[i][1] for i in range(2)):
            return "IMPOSSIBLE"
        if abs(sources[0][1]-sources[1][1]) < 1e-9:
            if abs(sources[0][1] - x) > 1e-8:
                return "IMPOSSIBLE"
            return v/(sources[0][0]+sources[1][0])
        V0,V1 = np.linalg.solve([[sources[0][1],sources[1][1]],[1,1]],[x*v,v])
        #print(V0,V1)
        return max(V0/sources[0][0],V1/sources[1][0])


t = int(raw_input())
for case in range(t):
    n, v, x = raw_input().split()
    n = int(n)
    v = float(v)
    x = float(x)
    sources = []
    for i in range(n):
        sources.append(list(map(float,raw_input().split())))
    #print(sources)
    print("Case #{0}: {1}".format(case+1,simple(sources,n,v,x)))