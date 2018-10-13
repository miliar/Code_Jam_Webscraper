#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:20:24 2017

@author: rcuriel

Problem B. Tidy Numbers
"""

def finding_Tidy(n):
    TidyNumber = -1
    nAux = int(n)
    isTidy = True
    for i in range(nAux,0,-1):
        nx = str(i)
        for j in range(len(nx)-1):
            if (nx[j] <= nx[j+1]):
                isTidy = True
            else:
                isTidy = False
                break
        if isTidy:
            TidyNumber = i
            break
    return  TidyNumber   
            
                
data_in = open('B-small-attempt0.in', 'r')
data_out = open('PB_CodeJam2017_out.txt','w')

T = int(data_in.readline())

for i in range(T):
    N = data_in.readline().strip()
    TidyNumber = finding_Tidy(N)
    print('Case #{}: {}'.format(i+1, TidyNumber), file=data_out)
    print('Case #{}: {}'.format(i+1, TidyNumber))
    