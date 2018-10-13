#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

f = open('A-large.in','r')
g = open('A-large.ou','w')



n = int(f.readline()[:-1])
for k in range(n):
    line = f.readline()[:-1].split(' ')
    D = int(line[0])
    N = int(line[1])
    T = 0
    for i in range(N):
        line_i = f.readline()[:-1].split()
        Ki = float(line_i[0])
        Si = float(line_i[1])
        Ti = (D-Ki)/Si
        T = max(T,Ti)
    S = D/T
    g.write('Case #'+str(k+1)+': '+str(S)+'\n')



f.close()
g.close()