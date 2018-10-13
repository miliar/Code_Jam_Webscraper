# -*- coding: utf-8 -*-
"""
Problem B. 
uses python 3.4.1

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
    n, v, x = readflds(f, (int, float))
    rc = [readflds(f, (float,)) for _ in range(n)]
    return n, v, x, rc

def solvecase(case):
    n, v, x, rc = case
    hot = [(c1, r1) for r1, c1 in rc if c1 > x]
    warm = [(c1, r1) for r1, c1 in rc if c1 == x]
    cold = [(c1, r1) for r1, c1 in rc if c1 < x]
    if not warm and (not hot or not cold):
        return 'IMPOSSIBLE'
    if warm and (not hot or not cold):
        return v / sum(r for c, r in warm)
    hotflow = sum(r*(c-x) for c, r in hot)
    coldflow = sum(r*(x-c) for c, r in cold)
    if hotflow == coldflow:
        fhot = [1] * len(hot)
        fcold = [1] * len(cold)
    elif hotflow < coldflow:
        fhot = [1] * len(hot)
        fcold = getfrac(coldflow-hotflow, [(x-c, r) for c, r in cold])
    else:
        fcold = [1] * len(cold)
        fhot = getfrac(hotflow-coldflow, [(c-x, r) for c, r in hot])
    rate = (sum(r for c, r in warm) +
            sum(f*r for (c, r), f in zip(cold, fcold)) +
            sum(f*r for (c, r), f in zip(hot, fhot))
            )
    return v/rate

def getfrac(flow, cr):
    ordered = sorted((c, r, i) for i, (c, r) in enumerate(cr))
    frac = [1] * len(cr)
    for c, r, i in reversed(ordered):
        if c*r >= flow:
            frac[i] = 1 - flow/(c*r)
            return frac
        else:
            frac[i] = 0
            flow -= c*r
	
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
    with open(argv[1]) as f, open('out', 'w') as out:
        cases = int(f.readline())
        for ncase in range(1, cases+1):
            case = readcase(f)
            soln = solvecase(case)
            if len(argv) > 2:
                print('Case #%d: %s' % (ncase, soln))
            print('Case #%d: %s' % (ncase, soln), file=out)

from datetime import datetime

start = datetime.now()
print(str(start))
main()
stop = datetime.now()
print(str(stop-start))
