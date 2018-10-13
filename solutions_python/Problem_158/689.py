#!/usr/bin/python2
import sys
import multiprocessing
import logging
import os
import itertools
import math
import gmpy2
import copy
import collections
import string
import scipy.stats as stats


def solve(casedata):
    """ Solve case """
    X, R, C = casedata
    if (R*C) % X != 0 or X > R*C:
        return "RICHARD"
    if X == 1:
        return "GABRIEL"
    if X == 2:
        return "GABRIEL"
    # piece too long for grid
    if X > R and X > C:
        return "RICHARD"
    # grid too small for 1 piece
    l = (X-1)/2 + 1
    L = X-l+1
    if min(R, C) < l or max(R, C) <= L:
        return "RICHARD"
    #if min(R, C) <= l + l or max(R, C) <= L + l:
    #    return "RICHARD"
    # holes
    if X >= 7 and (R > 2 and C > 2):
        ##
        # #
        ###
        return "RICHARD"
    if X > R+2 and X > C+2:
        # oo
        #  oooooo
        # oo
        return "RICHARD"
    # square block
    if X >= 4 and (R <= 3 and C <= 3):
        # 2x2 square
        return "RICHARD"
    if X >= 4 and (R == 2 or C == 2):
        # oo
        #  oo
        return "RICHARD"
    return "GABRIEL"


def parse():
    """ Returns a list of N lists containing imput data for each case """
    t = int(sys.stdin.readline())
    cases = list()
    for case in range(t):
        mountain = list()
        caves = {}
        X, R, C = map(int, sys.stdin.readline().rstrip('\n').split())
        casedata = [X, R, C]
        cases.append(casedata)
    return cases

if __name__ == '__main__':
    cases = parse()
    #p = multiprocessing.Pool(multiprocessing.cpu_count())
    #results = p.map(solve, cases)
    #for case, result in enumerate(results):
    #    print('Case #%d: %s' % (case + 1, result))
    #    sys.stdout.flush()

    #for case, data in enumerate(cases):
    #    result = solve(data)
    #    print('Case #%d: %s' % (case + 1, result))
    #    #sys.stdout.flush()

    p = multiprocessing.Pool(multiprocessing.cpu_count())
    resultobjs = [p.apply_async(solve, [case]) for case in cases]
    for case, resultobj in enumerate(resultobjs):
        print('Case #%d: %s' % (case + 1, resultobj.get()))
        sys.stdout.flush()
