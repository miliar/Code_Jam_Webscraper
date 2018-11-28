#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

'''f = open('C-large.in','r')
g = open('C-large.ou','w')'''

'''f = open('C-small-attempt0.in','r')
g = open('C-small-attempt0.ou','w')'''

f = open('C-small-2-attempt0.in','r')
g = open('C-small-2-attempt0.ou','w')


def solution(N,K):
    k = np.floor(np.log2(K))
    X = np.floor( (N-(2**k-1))/(2**k) )
    m = N - (2**k-1) - 2**k*X
    if K <= 2**k - 1 + m:
        p = X//2
        if X%2 == 0:
            x = p
            y = p
        else:
            x = p
            y = p+1
    else:
        p = (X-1)//2
        if X%2 == 1:
            x = p
            y = p
        else:
            x = p
            y = p+1
    return str(int(y)) + " " + str(int(x))



n = int(f.readline()[:-1])
for k in range(n):
    line = f.readline()[:-1].split()
    N = int(line[0])
    K = int(line[1])
    g.write('Case #'+str(k+1)+': '+solution(N, K)+'\n')



f.close()
g.close()
