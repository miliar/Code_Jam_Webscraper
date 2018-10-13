#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:14:33 2017

@author: dittaya
"""

import math

fout = open('C-2.out', 'w')
#with open('test.txt') as f:
with open('C-small-2-attempt1.in') as f:
    T = int(f.readline().strip())
    for nCase in range(T):
        line = f.readline()

        N,K = line.strip().split()
        N = int(N)
        K = int(K)
        
        h = int(math.log(K,2))
        
        filled = 2 ** h - 1
        slot = (N - filled) // (2 ** h)
        left = (N - filled) % (2 ** h)
        
        if left > 0 and (K - filled) <= left:
            slot += 1

        if slot % 2 != 0:
            smin = smax = slot // 2
        else:
            smin = (slot-1) // 2
            smax = smin+1
            
        
        print('Case #'+str(nCase+1)+':', smax, smin, file=fout)
fout.close()