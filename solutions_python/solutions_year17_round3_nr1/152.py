
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


# In[6]:

def solve(*args):
    print(args)


# In[16]:

def height_score(pa):
    return 2* math.pi*pa[1]*pa[0]

def surface_score(pa):
    return math.pi*pa[0]*pa[0]

def solve(N,K,p):
    surfaces = [surface_score(pa) for pa in p]
    m = max(surfaces)
    surface = surfaces.index(m)
    
    heights = [height_score(pa) for pa in p]
    pheights = sorted(heights, reverse=True)
    ph = sorted(range(N), key=lambda x:heights[x],reverse=True)
    
    return max([sum(pheights[:K]) + surfaces[i] if i in ph[:K] else sum(pheights[:K - 1]) + heights[i] + surfaces[i] for i in range(N)])


# In[18]:

path = r'E:\Downloads\A-small-attempt0.in'

with open(path, 'r') as f, open(path[:-2]+'out', 'w') as outf:
    T = int(f.readline())
    for test_index in range(T):
        N, K = [int(x) for x in f.readline().strip().split()]
        p = [[int(x) for x in f.readline().strip().split()] for _ in range(N)]
        outf.write('Case #{}: {}\n'.format(test_index+1, solve(N,K,p)))

