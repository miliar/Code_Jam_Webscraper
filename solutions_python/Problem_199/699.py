"""Usage:
    pypy -u X.py < X-test.in > X-test.out
or sometimes:
    python -u X.py < X-test.in > X-test.out
may be python 2 or 3.
"""
from __future__ import print_function

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
    #S = [next(infile).strip() for _ in range(N)]
    del infile
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

    S, K = T[0], int(T[1])

    res = 0
    s = S
    for i in range(len(S) - K + 1):
        if s[0] == '-':
            s = ''.join('+' if c=='-' else '-' for c in s[1:K]) + s[K:]
            res += 1
        else:
            s = s[1:]

    if set(s) != set(['+']):
        res = 'IMPOSSIBLE'

    return 'Case #{:d}: {}'.format(tc, res)


if __name__ == '__main__':
    common_setup()
    cases = [case_reader(tc, sys.stdin) for tc in range(1, int(next(sys.stdin)) + 1)]
    for case in cases:
        print(case_solver(**case))
