# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
def a():
    n = max(z)
    if n % 2 == 0:
        if n /2 in z:
            z[n / 2] += 1
        else:
            z[n / 2] = 1
        
        if n / 2 - 1 in z:
            z[n / 2 - 1] += 1
        else:
            z[n / 2 - 1] = 1    
    
    else:
        if int(n/2) in z:
            z[int(n/2)] +=2
        else:
            z[int(n/2)] = 2
    z[n] -= 1
    if z[n] == 0:
        del z[n]

def b(m):
    if  m == 0:
        return 0,0
    elif m % 2 == 1:
        return int(m/2),int(m/2)
    else:
        return m/2 - 1, m/2 
    

t = int(input())
N = np.zeros(t)
S = np.zeros(t) # read a line with a single integer

for i in np.arange(t):
  N[i], S[i] = [int(s) for s in input().split(" ")]

for i in np.arange(t):
    z = {N[i]:1}
    for j in np.arange(S[i] - 1):
        a()
    minmax = b(max(z))
    print('Case #'+str(i+1) + ':',int(minmax[1]),int(minmax[0]))
