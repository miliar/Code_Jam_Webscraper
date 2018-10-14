#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

"""f = open('C-test.in','r')
g = open('C-test.ou','w')"""

f = open('C-small-1-attempt0.in','r')
g = open('C-small-1-attempt0.ou','w')

"""f = open('C-large.in','r')
g = open('C-large.ou','w')"""


def solution(N, K, U, P):
    while (U > 0.00001):
        k = np.argmin(P)
        P[k] += 0.0001
        U -= 0.0001
    res = 1
    for i in range(len(P)):
        res *= P[i]
    return res

n = int(f.readline()[:-1])
for k in range(n):
    line = f.readline()[:-1].split(' ')
    N = int(line[0])
    K = int(line[1])
    U = float(f.readline()[:-1])
    line_P = f.readline()[:-1].split()
    P = np.array([float(x) for x in line_P])
    g.write('Case #'+str(k+1)+': '+str(solution(N, K, U, P))+'\n')



f.close()
g.close()