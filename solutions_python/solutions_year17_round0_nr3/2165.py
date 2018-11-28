#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Submission for problem C: Bathroom Stalls
of Google CodeJam 2017

Author: Christos Tsirigotis <tsirif@gmail.com>
Date: April 09, 2017
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
    T = int(input())  # get number of test cases
    for nc in range(1, T + 1):
        N, K = list(map(int, input().split()))  # get list of numbers
        k = int(np.floor(np.log2(K + 1)))
        symmetrics = 2**k - 1
        if symmetrics == K:
            if K == 1:
                left_after_inclusion = (N - K) / 2**k
            else:
                ssymm = 2**(k-1) - 1
                aver_space_left = (N - ssymm) / 2**(k-1)
                space_chosen = np.floor(aver_space_left)
                left_after_inclusion = (space_chosen - 1) / 2
        else:
            ratio = (K - symmetrics) / 2**k  # how many left over full power row
            aver_space_left = (N - symmetrics) / 2**k
            most_space_left_ratio = aver_space_left - np.floor(aver_space_left)
            if ratio > most_space_left_ratio:  # if big space seats taken
                space_chosen = np.floor(aver_space_left)
            else:
                space_chosen = np.ceil(aver_space_left)
            left_after_inclusion = (space_chosen - 1) / 2
        maxof = int(np.ceil(left_after_inclusion))
        minof = int(np.floor(left_after_inclusion))
        out(nc, [maxof, minof])


solve()
