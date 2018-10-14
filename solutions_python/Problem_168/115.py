# -*- coding: utf-8 -*-
"""
Problem A. 
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
    charmap = {'.':None,
               '^':(-1, 0),
               '>':(0, 1),
               '<':(0, -1),
               'v':(1, 0)
               }
    rows, cols = readints(f)
    ans = [f.readline().strip() for _ in range(rows)]
    assert all(len(row) == cols for row in ans)
    assert all(c in '.^v<>' for row in ans for c in row)
    return ans

def solvecase(mtx):
    tmtx = list(zip(*mtx))
    counts = (rowcheck(mtx, tmtx, '<', '>'),
              rowcheck(tmtx, mtx, '^', 'v'))
    if None in counts:
        return 'IMPOSSIBLE'
    else:
        return sum(counts)

def rowcheck(mtx, tmtx, lo, hi):    
    count = 0
    okswitch = [1 < sum(c != '.' for c in col) for col in tmtx]
    for rownum, row in enumerate( mtx):
        arrlocs = [i for i, x in enumerate(row) if x != '.']
        if len(arrlocs) == 0:
            continue
        for p, c in [(0, lo), (-1, hi)]:
            if row[arrlocs[p]] == c:
                count += 1
            if len(arrlocs)==1 and not okswitch[arrlocs[p]]:
                return None
    return count
	
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
