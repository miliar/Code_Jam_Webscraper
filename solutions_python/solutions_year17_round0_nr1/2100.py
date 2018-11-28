#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Submission for problem A: Oversized Pancake Flipper
of Google CodeJam 2017

Author: Christos Tsirigotis <tsirif@gmail.com>
Date: April 08, 2017
"""


from __future__ import absolute_import, print_function, division
import itertools as itools
from itertools import compress as cmpr
from itertools import product as prd
from itertools import permutations as perm
from itertools import combinations as comb
from itertools import combinations_with_replacement as combr
from fractions import gcd
from collections import defaultdict as dd
from collections import deque as dq
import numpy as np
from numpy import pi
bc = lambda n: bc((n - 1) & n) + 1 if n else 0
MOD = 1000002013
EPS = 1e-8

OUTCASE = "Case #%(nc)s:"
outlist = lambda x, y: print(x + ' ' + ' '.join(map(str, y)))
outnum = lambda x, y: print(x + ' ' + str(y))


def out(nc, solution):
    outcase = OUTCASE % locals()
    try:
        float(solution)
        outnum(outcase, solution)
    except TypeError:
        outlist(outcase, solution)


def solve():
    convert = lambda x: False if x == '-' else True
    flip = lambda x: not x
    K = 0

    def bfs(up, down, crepes_seen, flips):
        if not up:
            return False
        if len(up) > len(down):
            return bfs(down, up, crepes_seen, flips)
        crepes_seen |= (up | down)
        tmp = set()
        done = False
        while up:
            crepes = up.pop()
            for i in range(len(crepes) - K + 1):
                flipped = list(crepes)
                flipped[i:i+K] = list(map(flip, flipped[i:i+K]))
                flipped = tuple(flipped)
                if flipped in down:
                    done = True
                if not done and flipped not in crepes_seen:
                    tmp.add(flipped)
        flips[0] += 1
        return done or bfs(tmp, down, crepes_seen, flips)

    T = int(input())  # get number of test cases
    for nc in range(1, T + 1):
        S, K = input().split()
        K = int(K)
        S = tuple(map(convert, S))
        up = set([S])
        finit = (True, ) * len(S)
        down = set([finit])
        flips = [0]
        if S in down:
            out(nc, flips[0])
        else:
            found = bfs(up, down, set(), flips)
            if found:
                out(nc, flips[0])
            else:
                outcase = OUTCASE % locals()
                print(outcase + ' IMPOSSIBLE')


solve()
