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

def solve(comb, opp, data):
    C = collections.defaultdict(dict)
    for a, b, c in comb:
        C[a][b] = c
        C[b][a] = c
    O = collections.defaultdict(set)
    for a, b in opp:
        O[a].add(b)
        O[b].add(a)
    cur = []
    for x in data:
        if cur and cur[-1] in C[x]:
            cur[-1] = C[x][cur[-1]]
            continue
        if O[x] and set(cur) & O[x]:
            cur = []
            continue
        cur.append(x)

    return '[{}]'.format(', '.join(cur))

def go():
    t = gcj.token(int)
    for _ in xrange(t):
        c = gcj.token(int)
        combines = gcj.tokens(c)
        o = gcj.token(int)
        opposes = gcj.tokens(o)
        n = gcj.token(int)
        data = gcj.token()
        assert len(data) == n
        print gcj.case(), solve(combines, opposes, data)

go()
