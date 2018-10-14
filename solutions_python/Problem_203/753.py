
# coding: utf-8

# In[1]:

import numpy as np
import itertools as it
import collections as col


# In[2]:

import sys
sys.setrecursionlimit(10000)


# In[3]:

import networkx as nx
import matplotlib.pyplot as plt


# In[44]:

def solve(*args):
    print(args)


# In[51]:

def solve(words, R,C):
    sol = np.asarray(words)

    while len(np.argwhere(sol == '?')) > 0:
        for row in range(R):
            for col in range(C):
                if sol[row][col] == '?':
                    if row > 0:
                        sol[row][col] = sol[row-1][col]

        for row in reversed(range(R)):
            for col in range(C):
                if sol[row][col] == '?':
                    if row < R -1:
                        sol[row][col] = sol[row+1][col]

        for col in range(C):
            for row in range(R):
                if sol[row][col] == '?':
                    if col > 0:
                        sol[row][col] = sol[row][col-1]

        for col in reversed(range(C)):
            for row in range(R):
                if sol[row][col] == '?':
                    if row < C -1:
                        sol[row][col] = sol[row][col+1]
    
    return '\n' + '\n'.join([''.join(r) for r in sol])


# In[53]:

path = r'C:\Users\Shachar\Downloads\A-small-attempt2.in'

with open(path, 'r') as f, open(path[:-2]+'out', 'w') as outf:
    T = int(f.readline())
    for test_index in range(T):
        R,C = [int(x) for x in f.readline().split()]
        words = [list(f.readline().strip()) for _ in range(R)]
        outf.write('Case #{}: {}\n'.format(test_index+1, solve(words,R,C)))

