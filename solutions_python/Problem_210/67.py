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
    [C, J] = casedata
    C.sort()
    J.sort()
    chgs = 0
    lC, lJ = len(C), len(J)
    lT = lC + lJ
    Ctime = 720 - sum([x[1]-x[0] for x in C])
    Jtime = 720 - sum([x[1]-x[0] for x in J])
    actp = []
    idxc = 0
    idxj = 0
    nochgC = []
    nochgJ = []
    while idxc+idxj < lT:
        if idxj == lJ or (idxc < lC and C[idxc][0] < J[idxj][0]):
            actp.append(1)
            if len(actp)>1 and actp[-2] == 1:
                if C[idxc][0]-C[idxc-1][-1] > Ctime:
                    chgs += 2
                else:
                    nochgC.append(C[idxc][0]-C[idxc-1][-1])
            idxc += 1
        else:
            actp.append(2)
            if len(actp)>1 and actp[-2] == 2:
                if J[idxj][0]-J[idxj-1][-1] > Jtime:
                    chgs += 2
                else:
                    nochgJ.append(J[idxj][0]-J[idxj-1][-1])
            idxj += 1
    if len(actp) > 1:
        # check around midnight - same person
        if actp[0] == actp[-1]:
            if actp[0] == 1:
                # C has 1st and last activity
                if C[0][0] - (C[-1][1] - 1440) > Ctime:
                    chgs += 2
                else:
                    nochgC.append(C[0][0] - (C[-1][1] - 1440))
            else:
                if J[0][0] - (J[-1][1] - 1440) > Jtime:
                    chgs += 2
                else:
                    nochgJ.append(J[0][0] - (J[-1][1] - 1440))
        lastp = actp[-1]
        # count required changes
        for i in actp:
            if i != lastp:
                lastp = i
                chgs += 1
    nochgJ.sort()
    nochgC.sort()
    while True:
        if sum(nochgJ) <= Jtime:
            break
        else:
            chgs += 2
            nochgJ.pop()
    while True:
        if sum(nochgC) <= Ctime:
            break
        else:
            chgs += 2
            nochgC.pop()
    
    chgs = max(2, ((chgs + 1) / 2) * 2)
    return chgs

def parse():
    """ Returns a list of N lists containing imput data for each case """
    t = int(sys.stdin.readline())
    cases = list()
    for case in range(t):
        Ac, Aj = map(int, sys.stdin.readline().rstrip('\n').split())
        C = []
        J = []
        for i in range(Ac):
            C.append(map(int, sys.stdin.readline().rstrip('\n').split()))
        for i in range(Aj):
            J.append(map(int, sys.stdin.readline().rstrip('\n').split()))
        casedata = [C, J]
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
