#!/usr/bin/env python2.7
from __future__ import print_function
import itertools as itools
import operator

def read_case():
    raw_input()
    return map(int, raw_input().split())

# This problem was evil
def solve(case):
    ptotal = reduce(operator.xor, case)
    if ptotal != 0:
        return None
    else:
        return sum(case) - min(case)

def silly_solve(case):
    all = set(range(len(case)))
    best = 0
    for n in xrange(1, len(case)):
        for comb in itools.combinations(all, n):
            piles = set(comb), all - set(comb)
            sval = sum(case[i] for i in piles[1])
            if sval <= best:
                continue
            pvals = [reduce(operator.xor, (case[i] for i in piles[j])) \
                    for j in (0,1)]
            if pvals[0] == pvals[1]:
                best = sval
    return best

T = int(raw_input())
for casenum in xrange(1, T + 1):
    print("Case #{}: {}".format(casenum, solve(read_case()) or 'NO'))
