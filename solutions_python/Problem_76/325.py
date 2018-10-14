#!/usr/bin/env python3

import sys
from functools import reduce

T = int(sys.stdin.readline())

for case in range(T):
    N = int(sys.stdin.readline())
    C = list(map(int, sys.stdin.readline().rstrip().split()))
    if reduce(lambda x, y: x^y, C) == 0:
        print('Case #{0}:'.format(case+1), sum(C) - min(C))
    else:
        print('Case #{0}: NO'.format(case+1))
