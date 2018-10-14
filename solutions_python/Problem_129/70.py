# encoding: UTF-8

from __future__ import absolute_import, division

from future_builtins import *
range = xrange

import collections
import itertools
import sys

class gcj:
    IN = sys.stdin
    buf = None

    identity = lambda x: x

    @classmethod
    def _read_line_raw(cls):
        if cls.buf:
            res = cls.buf
            cls.buf = None
        else:
            res = cls.IN.readline()
        if not res:
            raise EOFError()
        return res

    @classmethod
    def _read_line_view(cls):
        line = cls._read_line_raw()
        if not isinstance(line, memoryview):
            line = memoryview(line)
        return line

    @classmethod
    def _read_line(cls):
        line = cls._read_line_raw()
        if isinstance(line, memoryview):
            line = line.tobytes()
        return line

    @classmethod
    def line(cls, conv=identity):
        line = cls._read_line()
        return conv(line.rstrip(b'\r\n'))

    @classmethod
    def splitline(cls, conv=identity):
        line = cls._read_line()
        return [conv(x) for x in line.split()]

    @classmethod
    def whitespace(cls):
        line = None
        while not line:
            line = cls._read_line_raw()
            i = 0
            l = len(line)
            while i < l and line[i].isspace():
                i += 1
            line = memoryview(line)[i:]
        cls.buf = line

    @classmethod
    def token(cls, conv=identity):
        cls.whitespace()
        line = cls._read_line_view()
        i = 0
        l = len(line)
        while i < l and not line[i].isspace():
            i += 1
        cls.buf = line[i:] if i < l else None
        return conv(line[:i].tobytes())

    @classmethod
    def tokens(cls, cnt, conv=identity):
        return [cls.token(conv) for _ in range(cnt)]

    current_case = 0

    @classmethod
    def case(cls):
        cls.current_case += 1
        return b'Case #{}:'.format(cls.current_case)

def cost(n, k):
    if k <= 0:
        return 0
    return (n + n-k+1)*k // 2

def solve(n, data):
    in_ = collections.defaultdict(int)
    out = collections.defaultdict(int)
    res = 0
    stations = set()
    for o, e, p in data:
        in_[o] += p
        out[e] += p
        res += p*cost(n, e-o)
        stations.add(o)
        stations.add(e)
    stations = sorted(stations)
    cur = []
    for (q, s) in enumerate(stations):
        i = in_[s]
        o = out[s]
        if i > 0:
            cur.append([i, n])
        while o > 0:
            x = min(o, cur[-1][0])
            o -= x
            if x == cur[-1][0]:
                cur.pop()
            else:
                cur[-1][0] -= x
        if q+1 < len(stations):
            d = stations[q+1] - s
            for x in cur:
                res -= x[0] * cost(x[1], d)
                x[1] -= d

    return res

def main():
    t = gcj.token(int)
    for _ in xrange(t):
        n, m = gcj.tokens(2, int)
        data = []
        for _ in xrange(m):
            o, e, p = gcj.tokens(3, int)
            data.append((o, e, p))
        print gcj.case(), solve(n, data) % 1000002013

main()
