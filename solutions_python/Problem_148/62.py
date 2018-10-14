# -*- coding: utf-8 -*-
"""
Problem A. 
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
    nfiles, cap = readints(f)
    files = sorted(readints(f))
    assert nfiles==len(files)
    return cap, files

def solvecase(case):
    cap, files = case
    ans = 0
    i, j = 0, len(files)-1
    while i < j:
        if files[i] + files[j] <= cap:
            i += 1
            j -= 1
            ans += 1
        else:
            j -= 1
            ans += 1
    if i == j:
        ans += 1
    return str(ans)
	
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
    with open('A-large.in') as f, open('out', 'w') as out:
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
