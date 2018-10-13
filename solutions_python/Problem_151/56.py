# -*- coding: utf-8 -*-
"""
Problem D. 
uses python 3.3

@author: Eric Kuritzky
"""
from collections import *
import itertools as ito
import operator as op
import functools as ft
from sys import argv, stdin, stdout, stderr, setrecursionlimit

#setrecursionlimit(1000000)

errprt = ft.partial(print, file=stderr)    
    
def readcase(f):
    nstr, nshard = readints(f)
    strs = [f.readline().strip() for _ in range(nstr)]
    return nshard, strs

def solvecase(case):
    nshard, strs = case
    worst = nties = 0
    for assign in ito.product(range(nshard), repeat=len(strs)):
        cost = getcost(strs, assign, nshard)
        if cost > worst:
            worst, nties = cost, 0
        elif cost == worst:
            nties += 1
    return '%d %d' % (worst, nties+1)

def getcost(strs, assign, nshard):
    astr = [[] for _ in range(nshard)]
    for i, s in enumerate(strs):
        astr[assign[i]].append(s)
    cost = 0
    for a in astr:
        cost += len(set(s[:i] for s in a for i in range(len(s)+1)))
    return cost
    
def readints(f):
    return list(map(int, f.readline().strip().split(' ')))

def readflds(f, types):
    if isinstance(types, tuple):
        return [typ(fld) for fld, typ
                in zip(f.readline().strip().split(),
                       ito.chain(types, ito.repeat(types[-1])))]
    else:
        return [types(fld) for fld in f.readline().strip().split()]

def main():
    with open('D-small-attempt0.in') as f, open('out', 'w') as out:
        cases = int(f.readline())
        for ncase in range(1, cases+1):
            case = readcase(f)
            soln = solvecase(case)
            print('Case #%d: %s' % (ncase, soln))
            print('Case #%d: %s' % (ncase, soln), file=out)

from datetime import datetime

start = datetime.now()
print(str(start))
main()
stop = datetime.now()
print(str(stop-start))
