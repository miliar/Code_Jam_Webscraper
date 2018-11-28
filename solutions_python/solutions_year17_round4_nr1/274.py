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


def solve(casedata):
    """ Solve case """
    [N, P, g] = casedata
    res = 0
    for k in list(g):
        if k % P == 0:
            res += g[k]
            del g[k]
    l = list(g.elements())
    unmatched = list()
    while len(l) > 1:
        # try to match #1 with one other element
        elem0 = l[0]
        notfound = True
        for i in l[1:]:
            if (i+elem0) % P == 0:
                l.remove(i)
                l.remove(elem0)
                res += 1
                notfound = False
                break
        if notfound:
            unmatched.append(elem0)
            l.remove(elem0)
    l = l + unmatched
    unmatched = list()
    while len(l) > 2:
        # try to match #1 with two other elements
        elem0 = l[0]
        notfound = True
        for idxi in range(1, len(l)-1):
            if notfound == False:
                break
            i = l[idxi]
            for idxj in range(idxi+1, len(l)-1):
                j = l[idxj]
                if (i+j+elem0) % P == 0:
                    l.remove(i)
                    l.remove(j)
                    l.remove(elem0)
                    res += 1
                    notfound = False
                    break
        if notfound:
            unmatched.append(elem0)
            l.remove(elem0)
    l = l + unmatched
    unmatched = list()
    while len(l) > 2:
        # try to match #1 with 3 other elements
        elem0 = l[0]
        notfound = True
        for idxi in range(1, len(l)-1):
            if notfound == False:
                break
            i = l[idxi]
            for idxj in range(idxi+1, len(l)-1):
                if notfound == False:
                    break
                j = l[idxj]
                for idxk in range(idxj+1, len(l)-1):
                    k = l[idxk]
                    if (i+j+k+elem0) % P == 0:
                        l.remove(i)
                        l.remove(j)
                        l.remove(k)
                        l.remove(elem0)
                        res += 1
                        notfound = False
                        continue
        if notfound:
            unmatched.append(elem0)
            l.remove(elem0)
    l = l + unmatched
    if len(l) >= 1:
        res += 1
    return res

def parse():
    """ Returns a list of N lists containing imput data for each case """
    t = int(sys.stdin.readline())
    cases = list()
    for case in range(t):
        N, P = map(int, sys.stdin.readline().rstrip('\n').split())
        g = collections.Counter()
        g.update(map(int, sys.stdin.readline().rstrip('\n').split()))
    
        casedata = [N, P, g]
        cases.append(casedata)
    return cases

if __name__ == '__main__':
    aparser = argparse.ArgumentParser()
    aparser.add_argument('-m', '--multiprocessing', action='store_true', default=False, required=False)
    aparser.add_argument('-t', '--test-parser', action='store_true', default=False, required=False)
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
