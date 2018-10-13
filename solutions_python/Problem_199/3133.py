#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 09:05:05 2017

@author: txmy
"""

n = int(input())
for i in range(n):
    sl = input().split()
    sl2 = list(sl[0])
    fl = int(sl[1])
    cnt = 0
    for j,s in enumerate(sl2):
        if(j + fl > len(sl2)):
            break
        if (s == '-'):
            cnt += 1
            for k in range(fl):
                if sl2[j+k] == '-':
                    sl2[j+k] = '+'
                else:
                    sl2[j+k] = '-'
    flg = False
    for m in range(fl):
        if sl2[-m] == '-':
            flg = True
    if(flg):
        print('Case #{0}: IMPOSSIBLE'.format(i+1))
    else:
        print('Case #{0}: {1}'.format(i+1,cnt))

        
                    
            
    