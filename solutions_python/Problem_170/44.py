
import math
import itertools
import numpy as np

from max_flow import *

################################################################################

def read_case(f):
    N = read_int(f)
    S = read_arr(f, N, read_words)
    return N, S

def solve_small(case):
    N, S = case
    best = None
    for i in range(10000):
        en = set(S[0])
        fr = set(S[1])
        for i in np.random.permutation(range(2, N)):
            s = set(S[i])
            e = len(s & en)
            f = len(s & fr)
            if e + f == 0:
                p = .5
            else:
                p = e / (e + f)
            if np.random.random() < p:
                en |= s
            else:
                fr |= s
        res = len(en & fr)
        if best is None or res < best:
            best = res
    return best
    # g = FlowNetwork()
    # for i in range(N):
    #     g.add_vertex(i)
    # for i in range(N):
    #     for j in range(N):
    #         if i == j:
    #             continue
    #         print(i, j, set(S[i]) & set(S[j]))
    #         g.add_edge(i, j, len(set(S[i]) & set(S[j])))
    # return g.max_flow(0, 1)

def solve_large(case):
    return solve_small(case)

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
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
