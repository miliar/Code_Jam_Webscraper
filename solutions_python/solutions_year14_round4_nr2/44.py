# -*- coding: utf-8 -*-
"""
Problem B. Up and Down
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
    n, = readints(f)
    a = readints(f)
    assert n == len(a)
    return a

def solvecase(a):
    rank2pos = [z for _,z in sorted((elt, n) for n, elt in enumerate(a))]
    n = len(rank2pos)
    left = right = 0
    cost = 0
    for i, pos in enumerate(rank2pos):
        leftcost = rank2pos[i] - left
        rightcost = n - 1 - right - rank2pos[i]
        side = rightcost < leftcost
#        print(side, leftcost, rightcost, cost)
        if side==0:
            cost += rank2pos[i] - left
            rank2pos[i], oldpos = left, rank2pos[i]
            for j in range(i+1, n):
                if rank2pos[j] < oldpos:
                    rank2pos[j] += 1
            left += 1
        else:
            newpos = n - 1 - right
            cost += newpos - rank2pos[i]
            rank2pos[i], oldpos = newpos, rank2pos[i]
            for j in range(i+1, n):
                if rank2pos[j] > oldpos:
                    rank2pos[j] -= 1
            right += 1
        assert len(set(rank2pos))==n and min(rank2pos)==0 and max(rank2pos)==n-1
##    oldcost = int(oldsolve(a))
##    assert cost == oldcost
    return str(cost)       

def oldsolve(a):
    cost = len(a)**2
    rank2pos = [z for _,z in sorted((elt, n) for n, elt in enumerate(a))]
    for assign in ito.product((0,1), repeat=len(a)-1):
        cost = min(asgcost(assign, rank2pos), cost)
    return str(cost)

def asgcost(assign, rank2pos):
    n = len(rank2pos)
    rank2pos = rank2pos.copy()
    left = right = 0
    cost = 0
#    print(rank2pos, assign)
    for i, side in enumerate(assign):
        if side==0:
            cost += rank2pos[i] - left
            rank2pos[i], oldpos = left, rank2pos[i]
            for j in range(i+1, n):
                if rank2pos[j] < oldpos:
                    rank2pos[j] += 1
            left += 1
        else:
            newpos = n - 1 - right
            cost += newpos - rank2pos[i]
            rank2pos[i], oldpos = newpos, rank2pos[i]
            for j in range(i+1, n):
                if rank2pos[j] > oldpos:
                    rank2pos[j] -= 1
            right += 1
#        print(rank2pos)
        assert len(set(rank2pos))==n and min(rank2pos)==0 and max(rank2pos)==n-1
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
    with open('B-large.in') as f, open('out', 'w') as out:
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
