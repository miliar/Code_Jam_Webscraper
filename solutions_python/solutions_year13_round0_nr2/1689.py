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
    (N, M) = read_ints(f)
    Cs = N*[None]
    for i in range(N):
        Cs[i] = read_ints(f)
    return ((N, M, Cs))
 
def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')
 
################################################################################

INF = float('inf')
 
import heapq

def check_rows(N, M, Cur):
    for i in range(N):
        Edge = Cur[i][0]
        if Edge == 'F':
            continue

        allpass = True
        for j in range(M):
            
            if Cur[i][j] == 'F':
                allpass = False
                break

        if allpass is True:
            for j in range(M):
                Cur[i][j] = 'T'

    return Cur

def check_cols(N, M, Cur):
    for j in range(M):
        Edge = Cur[0][j]
        if Edge == 'F':
            continue

        allpass = True
        for i in range(N):

            if Cur[i][j] == 'F':
                allpass = False
                break

        if allpass is True:
            for i in range(N):
                Cur[i][j] = 'T'

    return Cur


 
def solve_small(case):
    (N, M, Cs) = case
    print Cs

    res = N*[None]
    for i in range(N):
        res[i] = M*['F']
    print res

    Ds = {}
    for i in range(N):
        for j in range(M):
            key = Cs[i][j]
            if key not in Ds:
                Ds[key] = []
            Ds[key].append((i,j))

    for key in Ds.keys():
        Lawns = Ds[key]
        print Lawns
        for Lawn in Lawns:
            (I, J) = Lawn
            res[I][J] = 'O'

        print res
        res = check_rows(N, M, res)
        res = check_cols(N, M, res)

        for i in range(N):
            for j in range(M):
                # O should be turn into T
                if(res[i][j] == 'O'):
                    return "NO"


    

        




    return "YES"

solve_large = solve_small

solve(solve_small, "Lawnmower")
