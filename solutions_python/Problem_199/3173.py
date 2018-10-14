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
    (S, K) = read_words(f)
    K = int(K)
    print (S, K)
    return (S, K)
 
def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')
 
################################################################################

INF = float('inf')
 
import heapq

def flip(S, o, k):
    chars = []
    for c in S:
        chars.append(c)

    # print chars
    for i in range(o, o+k):
        if chars[i] == "+":
            chars[i] = "-"
        else:
            chars[i] = "+"

    return ''.join(chars)

def verify(S):
    chars = []
    for c in S:
        chars.append(c)

    res = True
    for i in range(len(S)):
        if chars[i] == "-":
            res = False
            break

    return res

def solve_small(case):
    (S, K) = case
    S_length = len(S)
    S_pattern = {}
    S_next = []
    flip_count = -1

    S_next.append(S)
    S_pattern[S] = 0

    while len(S_next) > 0:
        _S = S_next.pop(0)
        if verify(_S):
            flip_count = S_pattern[_S]
            break
        for i in range(S_length-K+1):
            _S_flip = flip(_S, i, K)

            if _S_flip not in S_pattern:
                S_pattern[_S_flip] = S_pattern[_S] + 1
                S_next.append(_S_flip)
            
        # print S_next
                

    if flip_count >= 0:
        return flip_count
    else:
        return "IMPOSSIBLE"



#solve_large = solve_small

def solve_large(case):
    

    return res




#solve(solve_small, "OversizedPancakeFlipper")
solve(solve_small, "OversizedPancakeFlipper")
