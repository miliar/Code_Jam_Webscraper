#!/usr/bin/env python

import collections

import math
import pdb
from pdb import set_trace as brk
import re
import sys

#sys.setrecursionlimit(50)

INPUT = "tiny"
INPUT = "B-large.in"
#INPUT = "B-small-attempt2.in"


def debug(*args):
    # return
    sys.stderr.write(str(args) + "\n")


class Memoize:

    def __init__(self, function):
        self._cache = {}
        self._callable = function

    def __call__(self, *args, **kwds):
        cache = self._cache
        key = self._getKey(*args, **kwds)
        try:
            return cache[key]
        except KeyError:
            cachedValue = cache[key] = self._callable(*args, **kwds)
            return cachedValue

    def _getKey(self, *args, **kwds):
        return kwds and (args, ImmutableDict(kwds)) or args    


def size_to_servings(ra, aa):
    # brk()
    aa *= 10
    min_a = ra * 9
    max_a = ra * 11
    v = int(aa // max_a)
    s = set()
    mn = 1e8
    mx = -1
    while v * min_a <= aa:
        if v * max_a >= aa >= v * min_a:
            mx = v
            mn = min(mn, v)
            #s.add(v)
        v += 1
    if len(s) > 0:
        assert min(s) == mn
        assert max(s) == mx
    debug("%2.1f %d %2.1f %d %2.1f" % (aa / max_a, mn, float(aa) / float(ra), mx, aa / min_a))
    return (mn, mx)


def fixup(s):
    l = []
    for s1 in s:
        l.append(sorted((a, b) for (a, b) in s1 if a <= b))
    return l


def do_trial(recipe, lines):
    debug(recipe, lines)
    servings = [[size_to_servings(ra, ps) for ps in line] for ra, line in zip(recipe, lines)]
    servings = fixup(servings)
    for s in servings:
        debug("***** ", s)
    count = 0
    while min(len(s) for s in servings) > 0:
        mn, mx = min(s[0] for s in servings)
        debug("CHECKING %d, %d" % (mn, mx))
        for s in servings:
            a, b = s[0]
            if b < mn or a > mx:
                break
        else:
            debug("GOT IT")
            count += 1
            for s in servings:
                s[:] = s[1:]
            continue
        for s in servings:
            if s[0] == (mn, mx):
                debug("REMOVING from %s" % s)
                s[:] = s[1:]
    return count


f = file(INPUT)
T = int(f.readline()[:-1])
for i in range(T):
    N, P = [int(x) for x in f.readline().split()]
    recipe = [int(x) for x in f.readline().split()]
    lines = []
    for _ in range(N):
        lines.append([int(x) for x in f.readline().split()])
    # if i == 84: brk()
    v = do_trial(recipe, lines)
    print "Case #%d: %s" % (i+1, v)
