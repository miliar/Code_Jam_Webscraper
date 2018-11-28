#!/usr/bin/python3

import sys

ncases = int(sys.stdin.readline().strip())

for t in range(1, ncases+1):
    values = sys.stdin.readline().split()
    smax = int(values[0])
    shy = [int(x) for x in values[1]]

    friends = 0
    up = 0

    for s in range(0, smax+1):
        if up < s:
            friends += s - up
            up += s - up
        up += shy[s]

    print("Case #{0}: {1}".format(t, friends))

