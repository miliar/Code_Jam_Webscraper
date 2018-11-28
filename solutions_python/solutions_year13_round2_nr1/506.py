#!/usr/bin/env python3

import sys

def solve(initial, motes):
    # count moves required
    for (i,m) in enumerate(motes):
        if initial > m:
            initial += m
        else:
            # decide to delete or create
            if initial == 1:
                return solve(initial, motes[i+1:]) + 1
            else:
                return min(solve(initial + (initial - 1), motes[i:]), solve(initial, motes[i+1:])) + 1

    return 0

cases = int(sys.stdin.readline().strip())
for i in range(cases):
    temp = sys.stdin.readline().strip().split()
    initial = int(temp[0])

    print("Case #{0}: {1}".format(i+1, solve(initial, sorted(map(int, sys.stdin.readline().strip().split())))))
