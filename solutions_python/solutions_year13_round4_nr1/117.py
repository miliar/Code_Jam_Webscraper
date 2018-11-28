#!/usr/bin/python
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
    [N, M, oepairs] = casedata
    nincome = 0
    fincome = 0
    oc = collections.Counter()
    ec = collections.Counter()
    result = list()
    for o, e, p in oepairs:
        if o == e:
            pass
        else:
            d = e - o
            nincome += int(d*(N-d/2+1/2))*p
        oc[o] += p
        ec[e] += p
    onboard = collections.Counter()
    for s in sorted(set(oc) | set(ec)):
        if oc[s] > ec[s]:
            # passengers enter the subway
            onboard[s] += oc[s] - ec[s]
        else:
            # passengers leave the subway
            nbpass = ec[s] - oc[s]
            origs = sorted(list(onboard), reverse=True)
            for orig in origs:
                leaving = min(nbpass, onboard[orig])
                onboard[orig] -= leaving
                nbpass -= leaving
                d = s - orig
                fincome += int(d*(N-d/2+1/2))*leaving
                if nbpass == 0:
                    break
    return (nincome-fincome) % 1000002013

def parse():
    """ Returns a list of N lists containing imput data for each case """
    t = int(sys.stdin.readline())
    cases = list()
    for case in range(t):
        oepairs = list()
        N, M = map(int, sys.stdin.readline().rstrip('\n').split())
        for pair in range(M):
            oepairs.append(map(int, sys.stdin.readline().rstrip('\n').split()))
        casedata = [N, M, oepairs]
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
