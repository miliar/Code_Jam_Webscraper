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

sys.setrecursionlimit(sys.getrecursionlimit()*3)

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

ex1 = {
'R': set( ('R',)),
'Y': set( ('Y',)),
'B': set( ('B',)),
'O': set( ('R','Y')),
'G': set( ('Y','B')),
'V': set( ('R','B')),
'': set()
}

ex2 = dict()
for k in ex1.keys():
    ex2[k] = set()
    for k2 in ex1.keys():
        if len(ex1[k] & ex1[k2])>0:
            ex2[k].add(k2)

def solve(N,horses,solution = ""):
    if len(solution) == 0:
        c = ''
    else:
        c = solution[-1]

    sorted_keys = sorted(horses.items(), key=operator.itemgetter(1),reverse=True)
    for k,v in sorted_keys:
        if horses[k]==0: continue
        if k in ex2[c]: continue
        if N==1:
            if k not in ex2[solution[0]]:
                return solution + k
        if N>1:
            h2 = copy.copy(horses)
            h2[k] -= 1
            s = solve(N-1,h2,solution+k)
            if s=="IMPOSSIBLE": continue
            return s
    return "IMPOSSIBLE"


T = int(sys.stdin.readline())
for t in range(1,T+1):
    horses = dict()
    N, R, O, Y, G, B, V = map(int,sys.stdin.readline().split())
    horses['R'] = R
    horses['O'] = O
    horses['Y'] = Y
    horses['G'] = G
    horses['B'] = B
    horses['V'] = V
    if max(R,Y,B)*2>N:
        solution = "IMPOSSIBLE"
    else:
        solution = solve(N,horses)
    print("Case #%i: %s" % (t,solution))
