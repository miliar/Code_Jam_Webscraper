
import math
import itertools
import numpy as NP
import networkx as NX
from bisect import bisect_left

################################################################################

def read_case(f):
    N, X = read_ints(f)
    S = read_ints(f)
    return N, X, S

def solve_small(case):
    N, X, S = case
    res = 0
    d = []
    for s in sorted(S, reverse=True):
        i = bisect_left(d, s)
        if i == len(d):
            d.append(X - s)
            res += 1
        else:
            d = d[:i] + d[i+1:]
    return res

def solve_large(case):
    return solve_small(case)

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%d'%res)
    f.write('\n')

################################################################################

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
    return [reader(f, *args, **kwargs) for i in range(R)]

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
                write_case(fo, i, res)

DEBUG = 'i'

from run import *
