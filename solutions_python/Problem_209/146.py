#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 09:53:08 2017

@author: marshi
"""

import numpy as np

def max_syrup(r,h,k,n):
    r = np.array(r)
    h = np.array(h)
    
    sort = r.argsort()[::-1]
    
    r,h = r[sort],h[sort]
    space = np.array([2*np.pi*r_*h_ for r_,h_ in zip(r,h)])
    candidate = []
    for start in range(k-n+1):
        up_space = np.pi*r[start]*r[start]
        if n > 1:
            side_space = space[start]+sum(sorted(space[start+1:])[-(n-1):])
        else:
            side_space = space[start]
        candidate.append(up_space+side_space)
        
    return max(candidate)


if 0:
    #t = int(input())
    
    k,n = 1000,1000
    
    r = np.random.randint(100, size=1000)
    h = np.random.randint(100, size=1000)
    print(max_syrup(r,h,k,n))
else:
    t = int(input())
    for i in range(t):
        k,n = map(int, input().split(' '))
        r,h = [],[]
        for _ in range(k):
            r_,h_ = map(int, input().split(' '))
            r.append(r_)
            h.append(h_)
        print("Case #%d: %.9f" % (i+1, max_syrup(r,h,k,n)))