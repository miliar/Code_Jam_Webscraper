"""Usage:
    pypy -u X.py < X-test.in > X-test.out
or sometimes
    python -u X.py < X-test.in > X-test.out
"""

import os
import sys
#sys.setrecursionlimit(20000)


def common_setup():
    #import memcache as mc
    #C = mc.Client(['127.0.0.1:11211'])
    pass


def case_reader(tc, infile):
    #N = int(next(infile))
    #P = map(int, next(infile).split())
    #I = [map(int, next(infile).split()) for _ in range(P[0])]
    T = next(infile).split()
    S = [map(float, next(infile).split()) for _ in range(int(T[0]))]
    return locals()


def case_solver(tc, N=None, P=None, I=None, T=None, S=None, **kwargs):
    #import collections as co
    #import functools32 as ft
    #import itertools as it
    #import math as ma
    #import networkx as nx
    #import numpy as np
    #import operator as op
    #import random as rn
    #import re
    #import scipy as sp
    #import heapq as hq
    #import memcache as mc
    #C = mc.Client(['127.0.0.1:11211'])

    N, V, T = int(T[0]), float(T[1]), float(T[2])
    if all(t > T for r, t in S) or all(t < T for r, t in S) or (len(S) == 1 and S[0][1] != T):
        return 'Case #{:d}: {}'.format(tc, 'IMPOSSIBLE')
    if len(S) == 1:
        res = V / S[0][0]
    elif len(S) == 2:
        if S[0][1] == S[1][1]:
            res = res = V / (S[0][0] + S[1][0])
        else:
            V0 = (V * T - V * S[1][1]) / (S[0][1] - S[1][1])
            V1 = (V * T - V * S[0][1]) / (S[1][1] - S[0][1])
            res = max(V0 / S[0][0], V1 / S[1][0])
    else:
        raise 'impossible'
    return 'Case #{:d}: {}'.format(tc, res)


if __name__ == '__main__':
    common_setup()
    cases = [case_reader(tc, sys.stdin) for tc in range(1, int(next(sys.stdin)) + 1)]
    for case in cases:
        print case_solver(**case)
