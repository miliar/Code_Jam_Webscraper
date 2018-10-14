#!/usr/bin/python2
import sys
import multiprocessing
import logging
import os
import itertools
import math
#import gmpy2
import copy
import collections
import string
import scipy.stats as stats


def solve(casedata):
    """ Solve case """
    (n, strs) = casedata
    minstrs = list()
    cnts = list()
    for i in range(n):
        minstr = ''
        lastc = strs[i][0]
        cnt = list()
        cn = 0
        for c in strs[i]:
            if lastc != c:
                minstr += lastc
                lastc = c
                cnt.append(cn)
                cn = 0
            cn += 1
        minstr += lastc
        cnt.append(cn)
        minstrs.append(minstr)
        cnts.append(cnt)
    if len(set(minstrs)) != 1:
        return "Fegla Won"
    nbsteps = 0
    for idx, c in enumerate(minstr):
        moy = int(round(float(sum([z[idx] for z in cnts])) / len(strs)))
        for cn in cnts:
            nbchars = cn[idx]
            nbsteps += math.fabs(nbchars - moy)

    return int(nbsteps)

def parse():
    """ Returns a list of N lists containing input data for each case """
    t = int(sys.stdin.readline())
    cases = list()
    for case in range(t):
        n = int(sys.stdin.readline())
        strs = list()
        for i in range(n):
            strs.append(sys.stdin.readline().rstrip('\n'))
        casedata = [n, strs]
        cases.append(casedata)
    return cases

if __name__ == '__main__':
    cases = parse()
    #p = multiprocessing.Pool(multiprocessing.cpu_count())
    #results = p.map(solve, cases)
    #for case, result in enumerate(results):
    #    print('Case #%d: %s' % (case + 1, result))
    #    sys.stdout.flush()

    for case, data in enumerate(cases):
        result = solve(data)
        print('Case #%d: %s' % (case + 1, result))
        sys.stdout.flush()

    #p = multiprocessing.Pool(multiprocessing.cpu_count())
    #resultobjs = [p.apply_async(solve, [case]) for case in cases]
    #for case, resultobj in enumerate(resultobjs):
    #    print('Case #%d: %s' % (case + 1, resultobj.get()))
    #    sys.stdout.flush()
