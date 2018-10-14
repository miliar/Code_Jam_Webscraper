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
import argparse
import operator
from functools import reduce


def solve(casedata):
    """ Solve case """
    [N, K, U, P] = casedata
    P.sort()
    # spend U
    if sum(P[-K:]) + U >= K:
        return 1.00000
    while U > 0:
        nbid = 1
        val = P[0]
        for idx, i in enumerate(P[1:]):
            if i == val:
                nbid += 1
            else:
                break
        if nbid == len(P):
            P = [val+U/nbid] * len(P)
            U = 0.0
        else:
            spend = min(P[idx+1]-val, U/nbid)
            P = [val + spend] * nbid + P[nbid:]
            U -= spend * nbid

    # compute proba
    proba = reduce(operator.mul, P, 1)
    return "%.06f" % proba

def parse():
    """ Returns a list of N lists containing imput data for each case """
    t = int(sys.stdin.readline())
    cases = list()
    for case in range(t):
        N, K = map(int, sys.stdin.readline().rstrip('\n').split())
        U = map(float, sys.stdin.readline().rstrip('\n').split())[0]
        P = map(float, sys.stdin.readline().rstrip('\n').split())
        casedata = [N, K, U, P]
        cases.append(casedata)
    return cases

if __name__ == '__main__':
    aparser = argparse.ArgumentParser()
    aparser.add_argument('-m', '--multiprocessing', action='store_true', default=False, required=False)
    aparser.add_argument('-t', '--test-parser', action='store_true', default=False, required=False)
    aparser.add_argument('-d', '--debug', action='store_true', default=False, required=False)
    args = aparser.parse_args()
    cases = parse()
    if args.test_parser:
        for c in cases:
            print(c)
        sys.exit(1)
    if args.multiprocessing:
        p = multiprocessing.Pool(multiprocessing.cpu_count())
        resultobjs = [p.apply_async(solve, [case]) for case in cases]
        for case, resultobj in enumerate(resultobjs):
            print('Case #%d: %s' % (case + 1, resultobj.get()))
            sys.stdout.flush()
    else:
        for case, data in enumerate(cases):
            result = solve(data)
            if args.debug:
                print(data)
            print('Case #%d: %s' % (case + 1, result))
            #sys.stdout.flush()
        p = multiprocessing.Pool(multiprocessing.cpu_count())

    #results = p.map(solve, cases)
    #for case, result in enumerate(results):
    #    print('Case #%d: %s' % (case + 1, result))
    #    sys.stdout.flush()


    #p = multiprocessing.Pool(multiprocessing.cpu_count())
    #resultobjs = [p.apply_async(solve, [case]) for case in cases]
    #for case, resultobj in enumerate(resultobjs):
    #    print('Case #%d: %s' % (case + 1, resultobj.get()))
    #    sys.stdout.flush()
