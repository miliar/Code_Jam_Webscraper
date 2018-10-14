#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:14:33 2017

@author: dittaya
"""

fout = open('B-large.out', 'w')
with open('B-large.in') as f:
    T = int(f.readline().strip())
    for nCase in range(T):
        line = f.readline()

        N = list(map(int, list(line.strip())))
        
        for c in range(len(N)-1,0,-1):
            if int(N[c-1]) > int(N[c]):
                for change in range(c,len(N)):
                    N[change] = 9
                N[c-1] -= 1
                    


        print('Case #'+str(nCase+1)+':', int(''.join(map(str,N))), file=fout)
fout.close()