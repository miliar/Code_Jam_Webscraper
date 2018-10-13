# coding: utf-8 
from __future__ import division
import itertools
import math
#import numpy

def read_word(f):
	return next(f).strip()

def read_int(f, b=10):
	return int(read_word(f), b)

def read_letters(f):
	return list(read_word(f))

def read_digits(f, b=10):
	return [int(x, b) for x in read_letters(f)]

def read_words(f, d=' '):
	return read_word(f).split(d)

def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]

def read_floats(f, d=' '):
    return [float(x) for x in read_words(f, d)]
 
def read_arr(f, R, reader=read_ints, *args, **kwargs):
    res = []
    for i in range(R):
        res.append(reader(f, *args, **kwargs))
    return res
 
def solve(solver, fn, out_fn=None):
    in_fn = fn + '.in'
    if out_fn is None:
        out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            T = read_int(fi)
            for i in range(T):
                case = read_case(fi)
                res = solver(case)
                write_case(fo, i+1, res)
 
def read_case(f):
    D = read_int(f)
    P = read_ints(f)
    print (D, P)
    return (D, P)
 
def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')
 
################################################################################

INF = float('inf')
 
import heapq
    
def getMin(case):
    (R, D, P, limit) = case

    #print (R, D, P)
    if not P:
        return R

    if R >= limit:
        return limit

    Pmax = max(P)
    if Pmax <= 3:
        return R+Pmax

    compareAll = []

    for i in range(1, int(Pmax/2)+1):
        NewP = list(P)
        
        NewP.remove(Pmax)
        KeepPmax = i
        NewP.append(KeepPmax)
        NewP.append(Pmax - KeepPmax)
        compareAll.append((R+1, len(NewP), NewP, limit))



    OldP = list(P)
    OldP = [int(x-1) for x in OldP if x > 1]
    compareAll.append((R+1, len(OldP), OldP, limit))
    print compareAll

    return min([getMin(casei) for casei in compareAll])
    #return min(getMin(NewCase2), getMin(NewCase1))
 
def solve_small(case):
    (D, P) = case
    R = 0
    limit = max(P)

    #while Pmax > 0:
    #    HalfPmax = int(Pmax/2)
    #    if HalfPmax >= 2:
    #        NewP = P
    #        NewP.remove(Pmax)
    #        NewP.append(HalfPmax)
    #        NewP.append(Pmax - HalfPmax)
    #        NewPmax = max(NewP)
    #    else:
    #        NewPmax = Pmax#

    #    if Pmax > (NewPmax + 1):
    #        P = NewP
    #    else:
    #       P = [(x-1) for x in P if x > 1]

    #    turn += 1;

    #    if P:
    #        Pmax = max(P)
    #    else:
    #        Pmax = 0

    #print turn
    panCake = (R, D, P, limit)
    res = getMin(panCake)
    return res

solve_large = solve_small

#def solve_large(case):
    

#    return res




solve(solve_small, "InfiniteHouseofPancakes")
