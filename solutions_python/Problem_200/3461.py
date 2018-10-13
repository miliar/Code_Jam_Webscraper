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
    N = read_int(f)
    return N
 
def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')
 
################################################################################

INF = float('inf')
 
import heapq

def verify(S):
    ints = []
    for c in S:
        ints.append(int(c))

    res = True
    for i in range(len(S)-1):
        if ints[i] > ints[i+1]:
            res = False
            break

    return res

def find(S):
    ints = []
    for c in S:
        ints.append(int(c))

    i = len(S)-1
    _carry = False

    while i >= 0:
        if _carry:
            for j in range(i+1, len(S)):
                ints[j] = 9

            ints[i] = ints[i] - 1
            if ints[i] < 0:
                ints[i] = 9
                _carry = True
                i = i - 1
                continue
            else:
                _carry = False


        if i > 0 and ints[i] < ints[i-1]:
            _carry = True
            # ints[i] = 9
        
        i = i - 1                

    chars = []
    for i in ints:
        char = chr(i + ord('0'));
        chars.append(char)

    _S = ''.join(chars)
    return int(_S)

def solve_small(case):
    N = case
    print N
    last = find(str(N))
    


    return last




#solve_large = solve_small

def solve_large(case):
    

    return res




#solve(solve_small, "TidyNumbers")
solve(solve_small, "TidyNumbers")
