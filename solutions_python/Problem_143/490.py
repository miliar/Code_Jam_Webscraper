#!/usr/bin/env python

import sys

cases = int(sys.stdin.readline())

for case in range(cases):
    n = (int(i) for i in sys.stdin.readline().strip().split(' '))
    a, b, k = n
    #a -= 1
    #b -= 1
    #k -= 1

    result = 0
    for i in range(a):
        for j in range(b):
            if i & j < k: result += 1
    print('Case #{}: {}'.format(case+1, result))
