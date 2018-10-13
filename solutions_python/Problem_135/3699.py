# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 20:37:36 2014

@author: Abhiinmathek

Google Code Jam
Q1: Magic Trick
"""
import numpy as np
inmat = open('Input.txt','r').read().splitlines()
N = int(inmat[0])
inmat=inmat[1:]
ans1,ans2 = np.zeros(N), np.zeros(N)
M1,M2 = np.zeros((N,4,4),dtype=np.int16), np.zeros((N,4,4),dtype=np.int16)

for i in range(N):
    ans1[i] = int(inmat[i*10]) -1
    ans2[i] = int(inmat[i*10 + 5]) -1
    M1[i] = [[int(k) for k in j.split()] for j in inmat[i*10+1:i*10+1+ 4]]
    M2[i] = [[int(k) for k in j.split()] for j in inmat[i*10+1 + 4 +1: (i+1)*10]]

fa = ''
for i in range(N):
    ans = np.intersect1d(M1[i][ans1[i]],M2[i][ans2[i]])
    if (len(ans)) == 1:
       fa += 'Case #{0}: '.format(i+1) + str(ans[0]) + '\n'
    elif (len(ans)) > 1:
        fa += 'Case #{0}: Bad magician!'.format(i+1)+ '\n'
    elif (len(ans)==0):
        fa += 'Case #{0}: Volunteer cheated!'.format(i+1)+ '\n'        
print fa.strip()
open('Output.txt','w').write(fa.strip())