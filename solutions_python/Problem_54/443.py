#! /usr/bin/env python
#
#   B. Fair Warning
#

from __future__ import print_function
from sys import stdin

N = int(stdin.readline())
for case in range(1, N+1):
    line = [int(x) for x in stdin.readline().split()]
    times = sorted(set(line[1:]))
    diffs = set()
    for i in range(len(times)-1):
        diffs.add(times[i+1] - times[i])
    diffs = sorted(diffs, reverse=True)
    while len(diffs) > 1:
        a, b = diffs[-2:]
        while b > 0:
            a, b = b, (a % b)
        del diffs[-1]
        diffs[-1] = a
    t = diffs[0]
    print("Case #{0}:".format(case), (t - times[0] % t) % t)
