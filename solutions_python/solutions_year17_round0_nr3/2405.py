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
 
################################################################################
 
def read_case(f):
    (N, K) = read_ints(f)
    return (N, K)
 
def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')
 
################################################################################

INF = float('inf')
 
import heapq



def calc(B, N):
    DP = N*[None]
    L = N*[None]
    R = N*[None]
    _left = -1
    _right = len(B)
    for i in range(N):
        if B[i] == 'O':
            _left = i
        else:
            L[i] = i - _left -1

        if B[N-i-1] == 'O':
            _right = N-i-1
        else:
            R[N-i-1] = _right - (N - i - 1) -1


    for i in range(N):
        if B[i] == 'O':
            DP[i] = 'O'
        else:
            DP[i] = (L[i], R[i])

    return DP

def choose(DP, N):
    _max = N*[0]
    _min = N*[0]

    for i in range(N):
        if DP[i] != 'O':
            (L, R) = DP[i]
            _max[i] = max(L, R)
            _min[i] = min(L, R)


    _max_min = max(_min)
    _B = {}
    for i in range(N):
        if _min[i] == _max_min:
            _B[i] = _max[i]

    select = max(_B, key=_B.get)

    # print (_max, _min)

    return (select, _max[select], _min[select]) 


    

def solve_small(case):
    (N, K) = case
    print (N, K)
    B = N*['.']

    for i in range(K):
        DP = calc(B, N)

        # print DP
        (b, y, z) = choose(DP, N)
        B[b] = 'O'


    res = str(y) + " " + str(z)
    return res




#solve_large = solve_small

def solve_large(case):
    

    return res




#solve(solve_small, "BathroomStalls")
solve(solve_small, "BathroomStalls")
