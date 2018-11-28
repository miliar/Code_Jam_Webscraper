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
    (A, B) = read_ints(f)
    return ((A, B))
 
def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')
 
################################################################################

INF = float('inf')
 
import heapq

def check_pal(N):
    Ds = [int(x, 10) for x in list(str(N))]
    #print Ds
    res = True
    for i in range(len(Ds)):
        if (i >= math.ceil(len(Ds)/2)):
            return res

        if Ds[i] != Ds[len(Ds)-1-i]:
            res = False

    return res

    

 
def solve_small(case):
    (A, B) = case
    print (A, B)
    res = 0

    sqrtA = int(math.ceil((math.sqrt(A))))
    sqrtB = int(math.floor((math.sqrt(B))))

    #print (sqrtA, sqrtB)

    for i in range(sqrtA, sqrtB + 1):
        N = i**2
        if check_pal(N) is True and check_pal(i) is True:
            print (i, N)
            res = res + 1






    return res

solve_large = solve_small

solve(solve_small, "FairnSquare")
