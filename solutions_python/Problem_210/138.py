#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 09:53:08 2017

@author: marshi
"""

def pp_small(ac,aj,c,d):
    if ac == 1 or aj == 1:
        return 2
    else:
        if c[0] > d[0]:
            c,d = d,c
        if (d[1] - c[0]) > 720 and (1440 - (d[0] - c[1]) > 720):
            return 4
        else:
            return 2

if 0:
    ac,aj = 2,0
    c = [180, 540]
    d = [900, 1260]
    
    print(pp_small(ac,aj,c,d))
else:
    t = int(input())
    for i in range(t):
        ac,aj = map(int, input().split(' '))
        c = list(map(int, input().split(' ')))
        if ac+aj == 1:
            d = None
        else:
            d = list(map(int, input().split(' ')))
        print("Case #%d: %d"%(i+1, pp_small(ac,aj,c,d)))