#!/usr/bin/env python

from __future__ import division

import collections
import itertools
import sys

class gcj:
    IN = sys.stdin
    number = 0

    @classmethod
    def case(cls):
        cls.number += 1
        return 'Case #%d:' % cls.number

    @classmethod
    def line(cls, type=str):
        line = cls.IN.readline()
        return type(line.strip('\n'))

    @classmethod
    def splitline(cls, type=str):
        line = cls.IN.readline()
        return [type(x) for x in line.split()]

def solve(oriDicts, paths):
    dicts = {}
    res = 0
    for d in oriDicts:
        dirs = d.split('/')
        s = ""
        for i in xrange(1, len(dirs)):
            s = s + "/" + dirs[i]
            dicts[s] = 1
    for path in paths:
        dirs = path.split('/')
        s = ""
        for i in xrange(1, len(dirs)):
            s = s + "/" + dirs[i]
            if not dicts.has_key(s):
                dicts[s] = 1
                res = res + 1
    return res

def go():
    t = gcj.line(int)
    for _ in xrange(t):
        n, m = gcj.splitline(int)
        nLines = [gcj.line() for _ in xrange(n)]
        mLines = [gcj.line() for _ in xrange(m)]
        r = solve(nLines, mLines)
        print gcj.case(), r

go()
