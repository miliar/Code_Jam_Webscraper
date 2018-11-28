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

def solve():
    day = 1440
    cnts = gcj.tokens(2, int)
    events = []
    for i in range(2):
        for _ in range(cnts[i]):
            (start, stop) = gcj.tokens(2, int)
            events.append((start, stop, i))
    events.sort()
    sums = [0, 0]
    free_gap = 0
    paid_gaps = [[], []]
    res = 0
    for i in range(len(events)):
        cur = events[i]
        next = events[(i + 1) % len(events)]
        gap = (next[0] - cur[1]) % day
        sums[cur[2]] += cur[1] - cur[0]
        if cur[2] == next[2]:
            paid_gaps[cur[2]].append(gap)
            sums[cur[2]] += gap
        else:
            free_gap += gap
            res += 1
            sums[0] += gap
    bigger = max(range(2), key=lambda i: sums[i])
    smaller = 1 - bigger
    assert sums[0] + sums[1] == day
    assert sums[bigger] >= sums[smaller]
    assert bigger != smaller
    diff = (sums[bigger] - sums[smaller]) // 2
    diff -= min(diff, free_gap)
    for gap in sorted(paid_gaps[bigger], reverse=True):
        if diff <= 0:
            break
        diff -= min(gap, diff)
        res += 2
    return res

def main():
    sys.setrecursionlimit(10000)
    t = gcj.token(int)
    for _ in xrange(t):
        print gcj.case(), solve()
        sys.stdout.flush()

main()
