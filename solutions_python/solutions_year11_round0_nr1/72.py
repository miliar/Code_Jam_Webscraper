#!/usr/bin/env python

from __future__ import division

import collections
import itertools
import sys
import operator
import functools

class gcj:
    IN = sys.stdin
    buf = ''
    cur_case = 0

    @classmethod
    def id(x):
        return x

    @classmethod
    def _read_line(cls):
        if cls.buf:
            res = cls.buf
            cls.buf = ''
        else:
            res = cls.IN.readline()
        if not res:
            raise EOFError()
        return res

    @classmethod
    def line(cls, conv=str):
        line = cls._read_line()
        return conv(line.rstrip('\r\n'))

    @classmethod
    def splitline(cls, conv=str):
        line = cls._read_line()
        return [conv(x) for x in line.split()]

    @classmethod
    def whitespace(cls):
        line = None
        while not line:
            line = cls._read_line().lstrip()
        cls.buf = line

    @classmethod
    def token(cls, conv=str):
        cls.whitespace()
        line = cls._read_line()
        spl = line.split(None, 1)
        res = spl[0]
        assert line.startswith(res)
        cls.buf = line[len(res):]
        return conv(res)

    @classmethod
    def tokens(cls, cnt, conv=str):
        return [cls.token(conv) for _ in xrange(cnt)]

    @classmethod
    def case(cls):
      cls.cur_case += 1
      return 'Case #{}:'.format(cls.cur_case)

def solve(data):
    rev = dict(O='B', B='O')
    pos = dict(O=1, B=1)
    last = dict(O=0, B=0)
    lim = dict(O=0, B=0)
    for r, p in data:
        o = rev[r]
        dist = abs(p - pos[r])
        pos[r] = p
        lim[o] = last[r] = max(last[r] + dist, lim[r]) + 1
    return max(last.itervalues())


def go():
    t = gcj.token(int)
    for _ in xrange(t):
        n = gcj.token(int)
        data = []
        for _ in xrange(n):
            r = gcj.token()
            p = gcj.token(int)
            data.append((r, p))
        print gcj.case(), solve(data)

go()
