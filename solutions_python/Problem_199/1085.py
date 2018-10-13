#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:14:33 2017

@author: dittaya
"""

fout = open('A-large.out', 'w')
with open('A-large.in') as f:
    T = int(f.readline().strip())
    for nCase in range(T):
        line = f.readline()
        S, K = line.strip().split()
        S = S.replace('+','1').replace('-','0')
        K = int(K)

        flip = 2**K-1

        n = 0        
        c = 0
        while c <= len(S)-K:
            if S[c] == '0':
                n += 1
                S = S[:c] + bin(int(S[c:c+K], 2) ^ flip)[2:] + S[c+K:]
            c+=1
        
        if int(S[c:],2) != 2**(K-1)-1:
            print('Case #'+str(nCase+1)+': IMPOSSIBLE', file=fout)
        else:
            print('Case #'+str(nCase+1)+': '+str(n), file=fout)
fout.close()