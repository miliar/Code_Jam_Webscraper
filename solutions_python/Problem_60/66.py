#! /usr/bin/env python
#
#   B. Picking Up Chicks
#

from __future__ import print_function

for case in xrange(1, int(raw_input())+1):
    nchicks, narrive, barn, time = map(int, raw_input().split())
    chicks = zip(map(int, raw_input().split()), map(int, raw_input().split()))
    canreach = [barn - pos <= spd * time for pos, spd in chicks]
    if len(filter(None, canreach)) < narrive:
        minswaps = "IMPOSSIBLE"
    else:
        swaps = [-1] * nchicks
        for i in xrange(nchicks-1, -1, -1):
            if canreach[i]:
                swaps[i] = 0
                for j in xrange(i+1, nchicks):
                    if not canreach[j]:
                        swaps[i] += 1
        minswaps = sum(sorted(filter(lambda x: x >= 0, swaps))[:narrive])
    print("Case #{0}:".format(case), minswaps)
