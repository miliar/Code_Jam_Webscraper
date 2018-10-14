#!/usr/bin/env python3

import sys

cases = int(sys.stdin.readline())
for case in range(1, cases + 1):
    max, values = sys.stdin.readline().strip().split()
    
    values = [int(v) for v in values]
    needed = 0
    standing = 0

    for i, v in enumerate(values):
        diff = i - standing
        if diff > 0:
            needed += diff
            standing += diff
        standing += v
    
    print('Case #{}: {}'.format(case, needed))
    
