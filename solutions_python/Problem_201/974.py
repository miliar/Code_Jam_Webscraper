#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Google Code Jam template

from __future__ import print_function, division, absolute_import, unicode_literals
import collections
import time
import sys
import os
import random
import numpy as np
import scipy as sp
import networkx as nx
from numba import jit
import heapq

class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result

def calc(N):
    m = (N-1)//2
    M = (N)//2
    return  M,m

@memoize
def solve(N,K):
    if N==K: return 0,0
    M,m = calc(N)
    if K==1: return M,m
    k1 = K//2
    k0 = K-1-k1
    if k0==k1:
        return solve(m,k0)
    else:
        return solve(M,k1)


T = int(sys.stdin.readline())
for t in range(1,T+1):
    # solve
    N,K = sys.stdin.readline().split()
    N,K=int(N),int(K)
    solution = solve(N,K)
    print("Case #%i: %s %s" % (t,*solution))
