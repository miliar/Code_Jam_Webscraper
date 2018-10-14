import os
import math
import copy
import sys
from collections import *
import itertools

os.chdir('/Users/Dana/Documents/0530')
f = open('A-large.in','r')
fo = open('A.out','w')
T = int(f.readline())
for ite in range(T):
    temp = str.split(f.readline())
    r,c = int(temp[0]), int(temp[1])
    m = [['']*c]*r
    for i in range(r):
        m[i] = list(f.readline())
        if ite<T-1:
            del m[i][c]
    #print(m)
    flag = True
    s = 0
    for i in range(r):
        for j in range(c):
            if (m[i][j]!='.') and flag:
                can = [False]*4
                can[0] = False
                for k in range(i):
                    if m[k][j]!='.':
                        can[0] = True
                can[1] = False
                for k in range(i+1,r):
                    if m[k][j]!='.':
                        can[1] = True
                can[2] = False
                for k in range(j):
                    if m[i][k]!='.':
                        can[2] = True
                can[3] = False
                for k in range(j+1,c):
                    if m[i][k]!='.':
                        can[3] = True
                #print(can)
                if can==[False,False,False,False]:
                    flag = False
                else:
                    if m[i][j]=='^' and can[0]:
                        pass
                    elif m[i][j]=='v' and can[1]:
                        pass
                    elif m[i][j]=='<' and can[2]:
                        pass
                    elif m[i][j]=='>' and can[3]:
                        pass
                    else:
                        s = s+1
    if flag:
        res = str(s)
    else:
        res = 'IMPOSSIBLE'
    #print(res)
    fo.write('Case #')
    fo.write(str(ite+1))
    fo.write(': ')
    fo.write(res)
    fo.write('\n')
fo.close()

