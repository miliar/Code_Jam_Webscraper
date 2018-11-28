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


def step(t, autonomy, speed, horses, dists, start, end):
    # recursive, not enough cuts - much too slow
    if start == end:
        return t
    else:
        for dstidx, dist in enumerate(dists[start]):
            if dist != -1.0:
                break
        tk, tnk = None, None
        nautonomy, nspeed = horses[start]
        if autonomy > dist:
            if nautonomy < autonomy or nspeed < speed:
                tk = step(
                    t+(dist/speed), autonomy-dist, speed,
                    horses, dists, dstidx, end)
        if horses[start][0] >= dist:
            if autonomy <= nautonomy or speed <= nspeed:
                tnk = step(
                    t+(dist/horses[start][1]), horses[start][0], horses[start][1],
                    horses, dists, dstidx, end)
        if tk is None:
            res = tnk
        elif tnk is None:
            res = tk
        else:
            res = min(tk, tnk)
        return res

def solve(casedata):
    """ Solve case """
    [N, horses, dists, start, end] = casedata
    t = 0.0
    tds = [(0.0, 0.0, 1.0)]
    for curidx in range(0, N-1):
        dist = dists[curidx][curidx + 1]
        bestt = 1e1000
        newtds = []
        for (t, d, s) in tds:
            bestt = min(bestt, t)
            if d < dist:
                # can't reach dest
                continue
            newtds.append((t+dist/s, d-dist, s))
        if horses[curidx][0] >= dist:
            newtds.append(
                (bestt+(dist/horses[curidx][1]),
                 horses[curidx][0]-dist,
                 horses[curidx][1]))
        # keep best horses only
        mind = 0
        for t, d, s in sorted(newtds):
            if d < mind:
                newtds.remove((t, d, s))
        tds = newtds
    return sorted(tds)[0][0]

def parse():
    """ Returns a list of N lists containing imput data for each case """
    t = int(sys.stdin.readline())
    cases = list()
    for case in range(t):
        N, Q = map(int, sys.stdin.readline().rstrip('\n').split())
        horses = []
        dists = []
        for i in range(N):
            horses.append(map(float, sys.stdin.readline().rstrip('\n').split()))
        for i in range(N):
            dists.append(map(float, sys.stdin.readline().rstrip('\n').split()))
        start, end = map(int, sys.stdin.readline().rstrip('\n').split())
        start -= 1
        end -= 1
        casedata = [N, horses, dists, start, end]
        cases.append(casedata)
    return cases

if __name__ == '__main__':
    aparser = argparse.ArgumentParser()
    aparser.add_argument('-m', '--multiprocessing', action='store_true', default=False, required=False)
    aparser.add_argument('-t', '--test-parser', action='store_true', default=False, required=False)
    args = aparser.parse_args()
    cases = parse()
    if args.test_parser:
        print('\n'.join([str(c) for c in cases]))
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
            sys.stdout.flush()
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
