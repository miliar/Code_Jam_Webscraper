#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Submission for problem B: Tidy Numbers
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
        A = int(input())  # get a number
        Al = list(map(int, str(A)))
        start = 0
        num = Al[0]
        lowered = False
        for i in range(len(Al) - 1):
            if Al[i + 1] < Al[i]:
                lowered = True
                break
            if Al[i + 1] > Al[i]:
                start = i + 1
                num = Al[i + 1]
        if lowered:
            if num == 1:
                num = 10
            Al[start] = num - 1
            Al[start + 1:] = [9] * (len(Al) - start - 1)
            if num == 10:
                Al = Al[1:]
        B = int(''.join(map(str, Al)))
        out(nc, B)


solve()
