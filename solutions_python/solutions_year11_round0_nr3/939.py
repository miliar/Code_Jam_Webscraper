#!/usr/bin/env python3

import sys
import re

T = int(sys.stdin.readline())
for testcase in range(1, T + 1):
    line = sys.stdin.readline()
    line = sys.stdin.readline()
    candies = [int(c) for c in re.findall(r'\d+', line)]
    sxor = 0
    for candy in candies:
        sxor^=candy
    if sxor == 0:
        print('Case #{}: {}'.format(testcase, sum(candies) - min(candies)))
    else:
        print('Case #{}: NO'.format(testcase))
