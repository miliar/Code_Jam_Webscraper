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


def nbopsm(l):
    nb = 0
    for i in range(len(l)):
        m = min(l[i:])
        midx = l.index(m)
        nb += l.index(m) - i
        l = l[0:i] + [m] + l[i:midx] + l[midx+1:]
    return nb

def nbopsM(l):
    nb = 0
    for i in range(len(l)):
        m = max(l[i:])
        midx = l.index(m)
        nb += l.index(m) - i
        l = l[0:i] + [m] + l[i:midx] + l[midx+1:]
    return nb

def isminmax(s):
    v = s[0]
    if len(s)==1:
        return True
    j=1
    while j<len(s) and s[j] > v:
        v = s[j]
        j += 1
    while j<len(s) and s[j] < v:
        v = s[j]
        j += 1
    return j > (len(s) - 1)

def solve(casedata):
    """ Solve case """
    [N, A] = casedata
    res=0
    i=0
    j=len(A)-1
    while True:
        if isminmax(A):
            return res
        m = min(A)
        mpos = A.index(m)
        if mpos > ((len(A)-1)/2):
            res += len(A)-1-mpos
        else:
            res += mpos
        A = A[:mpos] + A[mpos+1:]


def parse():
    """ Returns a list of N lists containing imput data for each case """
    t = int(sys.stdin.readline())
    cases = list()
    for case in range(t):
        N = map(int, sys.stdin.readline().rstrip('\n'))
        A = map(int, sys.stdin.readline().rstrip('\n').split(' '))
        casedata = [N, A]
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
    #    sys.stdout.flush()

    p = multiprocessing.Pool(multiprocessing.cpu_count())
    resultobjs = [p.apply_async(solve, [case]) for case in cases]
    for case, resultobj in enumerate(resultobjs):
        print('Case #%d: %s' % (case + 1, resultobj.get()))
        sys.stdout.flush()
