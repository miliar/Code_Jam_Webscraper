#!/usr/bin/env python

import collections

import math
import pdb
from pdb import set_trace as brk
import re
import sys

#sys.setrecursionlimit(50)

INPUT = "tiny"
INPUT = "A-large.in"
#INPUT = "A-small-attempt1.in"


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


def horz_exp(l):
    #brk()
    if all(c=='?' for c in l):
        return l
    for _ in range(len(l)):
        if l[_] != '?':
            break
    fl = l[_]
    l = (fl * _) + l[_:]
    for _ in range(_, len(l)):
        if l[_] == '?':
            l = l[:_] + fl + l[_+1:]
        else:
            fl = l[_]
    return l


def vert_exp(lines):
    for _ in range(len(lines)):
        if lines[_][0] != '?':
            fl = lines[_]
            break

    l = []
    for _ in range(len(lines)):
        if lines[_][0] != '?':
            fl = lines[_]
        l.append(fl)
    return l


def do_trial(lines):
    debug(lines)
    lines = [horz_exp(l) for l in lines]
    lines = vert_exp(lines)
    return '\n' + '\n'.join(lines)


f = file(INPUT)
T = int(f.readline()[:-1])
for i in range(T):
    R, C = [int(x) for x in f.readline().split()]
    lines = []
    for _ in range(R):
        lines.append(f.readline()[:-1])
    v = do_trial(lines)
    print "Case #%d: %s" % (i+1, v)
