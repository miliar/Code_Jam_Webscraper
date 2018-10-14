# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:06:59 2017

@author: Jo
"""
import numpy as np
T = int(input())
N = np.zeros(T)
S = np.zeros(T) # read a line with a single integer
K = []

for i in np.arange(T):
    N[i], S[i] = [int(s) for s in input().split(" ")]
    j = 0
    for k in np.arange(S[i]):
        n, s = [int(s) for s in input().split(" ")]
        if (N[i]-n)/s > j:
            j = (N[i]-n)/s
    K.append(N[i]/j)
    
for i in np.arange(len(K)):
    print ('Case #{0}: {1:.6f}'.format(i+1,K[i]))
        

    
