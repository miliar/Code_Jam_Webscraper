#!/usr/bin/env pypy

from __future__ import division

import os.path
import sys

fname, ext = os.path.splitext(sys.argv[0])

try:
    input = open(fname + '.in')
except IOError:
    input = sys.stdin

def readline():
    return next(input).strip()

def readvals(t):
    return map(t, readline().split())

def memoize(func):
    cache = {}
    def f(*args, **kw):
        key = func.__module__, func.__name__, args
        if kw:
            key += frozenset(kw.iteritems()),
        try:
            return cache[key]
        except KeyError:
            cache[key] = result = func(*args, **kw)
            return result
    f.cache = cache
    return f

def results(mat):
    n = len(mat)
    matches = [{} for _ in range(n)]
    for i in xrange(n):
        for j in xrange(n):
            res = mat[i][j]
            if res != '.':
                matches[i][j] = res == '1'

    results = [(sum(m.values()), len(m)) for m in matches]
    wp = [won / played for won, played in results]
    owp = [(sum((results[opp][0] - 1 + result) / (results[opp][1] - 1)
                for opp, result in played.iteritems())
            / len(played))
           for played in matches]
    oowp = [sum(owp[opp] for opp in played) / len(played)
            for played in matches]

    print wp, owp, oowp
    
    return [0.25 * WP + 0.5 * OWP + 0.25 * OOWP
            for WP, OWP, OOWP in zip(wp, owp, oowp)]

ncases = int(readline())
with open(fname + '.out', 'w') as out:
    for caseno in range(ncases):
        n = int(readline())
        mat = [readline() for i in xrange(n)]
        print >> out, 'Case #{}:'.format(caseno + 1)
        for x in results(mat):
            print >> out, x
#        print 'Case #{}: {}'.format(caseno + 1, _)
        sys.stdout.flush()
