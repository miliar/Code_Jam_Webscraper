
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


# In[36]:

def solve(*args):
    print(args)


# In[38]:

def solve(N,K,X,p):
    p.sort()
    p.append(1.0)
    p = np.array(p)
    
    i = 0
    while X > 0 and i in range(N):
        if p[i] == 1.0:
            break
        inext = np.searchsorted(p, p[i], side='right')-1
        to_add = p[inext+1] - p[inext]
        to_add = to_add if X > to_add * (inext+1) else X / (inext+1)
        X -= to_add * (inext+1)
        p[:inext+1] += to_add
        i = inext+1
    print(X,p)
    return np.prod(p)


# In[27]:

get_ipython().magic('pinfo np.searchsorted')


# In[40]:

path = r'E:\Downloads\C-small-1-attempt1.in'

with open(path, 'r') as f, open(path[:-2]+'out', 'w') as outf:
    T = int(f.readline())
    for test_index in range(T):
        N, K = [int(x) for x in f.readline().strip().split()]
        X = float(f.readline())
        p = [float(x) for x in f.readline().strip().split()]
        outf.write('Case #{}: {}\n'.format(test_index+1, solve(N,K,X,p)))

