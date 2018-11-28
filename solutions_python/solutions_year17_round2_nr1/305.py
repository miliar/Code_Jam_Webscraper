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

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))


def solve(D,N,Ki,Si):
    vmax = 1e15
    for i in range(N):
        t = (D-Ki[i])/float(Si[i])
        vmax = min(vmax, D/t)
    return vmax

T = int(sys.stdin.readline())
for t in range(1,T+1):
    D,N = sys.stdin.readline().split()
    D,N = int(D),int(N)
    Ki=[]
    Si=[]
    for i in range(N):
        k,s = sys.stdin.readline().split()
        Ki.append(int(k))
        Si.append(int(s))
    solution = solve(D,N,Ki,Si)
    print("Case #%i: %.8f" % (t,solution))


