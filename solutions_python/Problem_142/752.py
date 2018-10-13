#!/usr/bin/env python

import sys
import itertools
import pprint

def solve(N, d):
    msg = "Fegla Won"
    start = d[0]
    end = d[1]
    if start == end:
        return 0
    pv = start[0]
    c = 0
    start_arr = []
    for cv in start:
        if cv == pv:
            c += 1
        else:
            start_arr.append((pv, c))
            c = 1
        pv = cv
    start_arr.append((pv, c))
    pv = end[0]
    c = 0
    end_arr = []
    for cv in end:
        if cv == pv:
            c += 1
        else:
            end_arr.append((pv, c))
            c = 1
        pv = cv
    end_arr.append((pv, c))
    if len(start_arr) != len(end_arr):
        return msg
    res1 = 0
    for (i, (v, cnt)) in enumerate(start_arr):
        (ev, ecnt) = end_arr[i]
        if v != ev:
            return msg
        res1 += abs(cnt - ecnt)
    return res1

filename = sys.argv[1]

inp = open(filename.strip())
lines = inp.readlines()

i = 1
body = iter(lines[1:])
for line in body:
    (N,) = map(lambda i: int(i), line.strip().split(" "))
    d = []
    for k in range(N):
        d.append(body.next().strip())
    print "Case #%d: %s" % (i, solve(N, d))
    i += 1

