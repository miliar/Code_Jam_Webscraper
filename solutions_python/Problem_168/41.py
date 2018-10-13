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
    P = map(int, next(infile).split())
    #I = [map(int, next(infile).split()) for _ in range(P[0])]
    #T = next(infile).split()
    S = [next(infile).strip() for _ in range(P[0])]
    return locals()


def case_solver(tc, N=None, P=None, I=None, T=None, S=None, **kwargs):
    #import collections as co
    #import functools32 as ft
    #import itertools as it
    #import math as ma
    import networkx as nx
    #import numpy as np
    #import operator as op
    #import random as rn
    #import re
    #import scipy as sp
    #import heapq as hq
    #import memcache as mc
    #C = mc.Client(['127.0.0.1:11211'])

    R, C = P
    S = list(S)
    res = 0

    def walk(j, i, d):
        if d == '^':
            for jj in reversed(range(j)):
                if S[jj][i] != '.':
                    return S[jj][i]
            else:
                return 'X'
        elif d == 'v':
            for jj in range(j + 1, R):
                if S[jj][i] != '.':
                    return S[jj][i]
            else:
                return 'X'
        elif d == '<':
            for ii in reversed(range(i)):
                if S[j][ii] != '.':
                    return S[j][ii]
            else:
                return 'X'
        else:
            for ii in range(i + 1, C):
                if S[j][ii] != '.':
                    return S[j][ii]
            else:
                return 'X'

    for j in range(R):
        for i in range(C):
            if S[j][i] == '.':
                continue
            if walk(j, i, S[j][i]) == 'X':
                for d in ['^', '>', 'v', '<']:
                    if walk(j, i, d) != 'X':
                        res += 1
                        break
                else:
                    res = 'IMPOSSIBLE'
                    return 'Case #{:d}: {}'.format(tc, res)
                        
    return 'Case #{:d}: {}'.format(tc, res)


if __name__ == '__main__':
    common_setup()
    cases = [case_reader(tc, sys.stdin) for tc in range(1, int(next(sys.stdin)) + 1)]
    for case in cases:
        print case_solver(**case)
