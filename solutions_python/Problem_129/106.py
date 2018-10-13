
import math
import itertools
import numpy as NP
import heapq

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
                write_case(fo, i, res)

################################################################################

def read_case(f):
    [N, M] = read_ints(f)
    P = read_arr(f, M)
    return [N, M, P]

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%d'%res)
    f.write('\n')

################################################################################

def solve_small(case):
    [N, M, P] = case
    rev = 0
    for (o, e, p) in P:
        dist = e-o
        cost = (2*N-dist+1)*dist/2
        rev += p * cost
    o = sorted(((-p[0], p[2]) for p in P), reverse=True)
    e = sorted(((-p[1], p[2]) for p in P), reverse=True)
    i = 0
    j = 0
    ps = []
    res = 0
    while i < len(o):
        if o[i][0] >= e[j][0]:
            heapq.heappush(ps, o[i])
            i += 1
        else:
            while e[j][1] > 0:
                (s, p) = heapq.heappop(ps)
                ex = min(p, e[j][1])
                e[j] = (e[j][0], e[j][1]-ex)
                dist = s-e[j][0]
                cost = (2*N-dist+1)*dist/2
                res += ex * cost
                if ex < p:
                    heapq.heappush(ps, (s, p-ex))
            j += 1
    while j < len(e):
        while e[j][1] > 0:
            (s, p) = heapq.heappop(ps)
            ex = min(p, e[j][1])
            e[j] = (e[j][0], e[j][1]-ex)
            dist = s-e[j][0]
            cost = (2*N-dist+1)*dist/2
            res += ex * cost
            if ex < p:
                heapq.heappush(ps, (s, p-ex))
        j += 1
    return rev-res

def solve_large(case):
    return solve_small(case)

DEBUG = 'i'

from run import *
