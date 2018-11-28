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

def solve(order,K,*args,**kwargs):
    N=len(order)
    cnt = 0
    for i in range(N-K+1):
        if order[i] == False:
            cnt+=1
            for j in range(K):
                order[i+j] ^= True
    if not all(order): return "IMPOSSIBLE"
    return cnt

T = int(sys.stdin.readline())
for t in range(1,T+1):
    # solve
    order,K = sys.stdin.readline().split()
    K=int(K)
    order = [x=="+" for x in order]
    solution = solve(order,K)
    print("Case #%i: %s" % (t,solution))
