#!/usr/bin/python

from sys import stdin, stdout

T = int(stdin.readline().strip())

for case in range(1, T+1):
    stdin.readline()
    ms = map(int, stdin.readline().strip().split())

    # Method 1
    method_1 = sum([ max(0, x-y) for x,y in zip(ms[:-1], ms[1:]) ])

    # Method 2
    rate = max([ x-y for x,y in zip(ms[:-1], ms[1:]) ])
    method_2 = sum([ min(rate, x) for x in ms[:-1] ])

    stdout.write("Case #{:d}: {:d} {:d}\n".format(case, method_1, method_2))
