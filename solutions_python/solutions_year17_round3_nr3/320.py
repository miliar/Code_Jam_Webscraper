#!/usr/bin/python
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
import operator
import copy
import networkx as nx

sys.setrecursionlimit(sys.getrecursionlimit()*3)


def count_smallest(l):
    m = min(l)
    return sum([1 if x==m else 0 for x in l])

def solve(N,K,U,P):
    P=P[0:K]
    P=np.asarray(P)
    diff = np.zeros(shape=(K,),dtype=np.float64)
    for i in range(K-1):
        x = min((P[i+1]-P[i]),U/float(i+1))
        U = max(0.0,U-x*(i+1))
        diff[:i+1] += x
        if U==0:
            break
    P+=diff
    P=np.minimum(P+U/len(P),1.0)
    if min(P)==0: return 0
    return np.exp(np.sum(np.log(P)))


T = int(sys.stdin.readline())
for t in range(1,T+1):
    N,K = sys.stdin.readline().split()
    U = float(sys.stdin.readline())
    N,K = int(N),int(K)
    P = sorted(list(map(float,sys.stdin.readline().split())))
    solution = solve(N,K,U,P)
    print("Case #%i: %.9f" % (t,solution))
