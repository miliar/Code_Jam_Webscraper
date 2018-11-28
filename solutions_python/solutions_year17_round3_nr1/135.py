#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

'''f = open('A-test.in','r')
g = open('A-test.ou','w')'''

'''f = open('A-small-attempt0.in','r')
g = open('A-small-attempt0.ou','w')'''

f = open('A-large.in','r')
g = open('A-large.ou','w')

def solution(P, K):
    P.sort()
    while (len(P) != K):
        maxR = P[-1][0]
        if maxR != P[-2][0]:
            singleMaxR = True
        else:
            singleMaxR = False
        minS = np.inf
        argmin = None
        for k in range(len(P) - 1):
            minS = min(minS, 2*P[k][0]*P[k][1])
            if minS == 2*P[k][0]*P[k][1]:
                argmin = k
        if singleMaxR:
            minS = min(minS, 2*P[-1][0]*P[-1][1] + P[-1][0]**2 - P[-2][0]**2)
            if minS == 2*P[-1][0]*P[-1][1] + P[-1][0]**2 - P[-2][0]**2:
                argmin = -1
        else:
            minS = min(minS, 2*P[-1][0]*P[-1][1])
            if minS == 2*P[-1][0]*P[-1][1]:
                argmin = -1
        P.remove(P[argmin])
    res = 0
    for k in range(len(P)):
        res += 2 * np.pi * P[k][0]*P[k][1]
    res += np.pi * P[-1][0]**2
    return res

n = int(f.readline()[:-1])
for k in range(n):
    line = f.readline()[:-1].split(' ')
    N = int(line[0])
    K = int(line[1])
    P = []
    for i in range(N):
        line_i = f.readline()[:-1].split()
        Ri = float(line_i[0])
        Hi = float(line_i[1])
        P += [(Ri, Hi)]
    g.write('Case #'+str(k+1)+': '+str(solution(P, K))+'\n')



f.close()
g.close()