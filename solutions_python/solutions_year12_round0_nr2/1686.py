#!/usr/bin/env python
import sys

def read_number():
    return int(sys.stdin.readline())

for case in range(1, read_number() + 1):
    line = map(int, sys.stdin.readline().split())
    n, surprising, min_filter = line[:3]
    totals = line[3:]

    mins = map(lambda x: x / 3.0, totals)
    bests = map(lambda x: int(x) if x.is_integer() else int(x + 1), mins)
    almost = len(filter(lambda x: x != 0 and x == (min_filter - 1), bests))
    result = len(filter(lambda x: x >= min_filter, bests)) + min(surprising, almost)
    print("Case #%d: %s" % (case, result))
