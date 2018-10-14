#!/usr/bin/python

import sys
import functools
import operator
import math
from itertools import chain, combinations
from heapq import heappop, heappush, _siftup


def transform(s):
    cn = s[0]
    i = 1
    ts = []
    sp = ""
    for c in s[1:]:
        if c == cn:
            i += 1
        if c != cn:
            ts.append(i)
            sp += c
            i = 1
            cn = c
    ts.append(i)
    sp += cn
    return (ts, sp)

def ravg(ns):
    return int(round(float(sum(ns)) / float(len(ns))))

def solve(counts):
    count = 0
    for i in range(len(counts[0])):
        avg = ravg(map(lambda x: x[i], counts))
        count += sum(map(lambda x: abs(x[i] - avg), counts))
    return count

def main():
    for i in range(int(raw_input())):
        n = int(raw_input())
        counts = []
        ss = []
        for _ in range(n):
            (cs, s) = transform(raw_input().rstrip())
            counts.append(cs)
            ss.append(s)
        s = ss[0]
        result = ""
        for sp in ss[1:]:
            if s != sp:
                result = "Fegla Won"

        if not result:
            result = solve(counts)
        print ("Case #%s: %s" % (i+1, result))

if __name__ == '__main__':
    main()
