
# coding: utf-8

# In[1]:

import numpy as np
import itertools as it
import collections as col


# In[2]:

import sys
sys.setrecursionlimit(10000)


# In[4]:

import networkx as nx
import matplotlib.pyplot as plt


# In[1]:

def solve(*args):
    print(args)


# In[24]:

def solve(AC,AJ,C,J):
    if AC + AJ > 2:
        return 999
    
    if AC == AJ:
        return 2
    
    if AC > AJ:
        act = C
    else:
        act = J
        
    if len(act) == 1:
        return 2
    print(act)
    act.sort(key=lambda z: z[1])
    print(act)
    d1 = act[1][1]-act[0][0]
    
    if d1 <= 720:
        return 2
    
    d2 = (act[0][1] + 1440)-act[1][0]
    if d2 <= 720:
        return 2
    
    return 4
    


# In[19]:

solve(2,0,[[900,1260],[180,540]],[])


# In[25]:

path = r'E:\Downloads\B-small-attempt0.in'

with open(path, 'r') as f, open(path[:-2]+'out', 'w') as outf:
    T = int(f.readline())
    for test_index in range(T):
        AC, AJ = [int(x) for x in f.readline().strip().split()]
        C = [[int(x) for x in f.readline().strip().split()] for _ in range(AC)]
        J = [[int(x) for x in f.readline().strip().split()] for _ in range(AJ)]
        outf.write('Case #{}: {}\n'.format(test_index+1, solve(AC,AJ,C,J)))

