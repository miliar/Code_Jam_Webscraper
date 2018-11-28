# coding: utf-8 
from __future__ import division
import itertools
import math
import operator
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
 
################################################################################
 
def read_case(f):
    (D, N) = read_ints(f)
    KS = [None for i in range(N)]
    for i in range(N):
        (K, S) = read_ints(f)
        KS[i] = (K,S)
    
    # print (D, N, KS)
    return (D, N, KS)
 
def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')
 
################################################################################

INF = float('inf')
 
import heapq



def solve_small(case):
    (D, N, KS) = case
    A = {}
    for i in range(N):
        (K, S) = KS[i]
        _A = (D - K) / S
        A[i] = _A

    S_A = sorted(A.items(), key=operator.itemgetter(1), reverse=True)
    print S_A   

    # mx = 0
    # for p in S_A:
    #     (i, T) = S_A[p]
    #     (K, S) = KS[i]
    #     mx = D / T

    (i, T) = S_A[0]
    mx = D / T
    print mx
    

            
    res = mx
    


    return res




#solve_large = solve_small

def solve_large(case):
    

    return res




#solve(solve_small, "CruiseControl")
solve(solve_small, "CruiseControl")
