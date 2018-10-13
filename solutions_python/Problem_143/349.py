#!/usr/bin/env python

import sys

input = open(sys.argv[1]).readlines()
T = int(input.pop(0).rstrip())

def win(A, B, K):
    count = 0
    for i in range(A):
        for j in range(B):
            if i & j < K:
                count += 1
    return count

for case in range(1, T+1):
    A, B, K = [int(x) for x in input.pop(0).rstrip().split()]
    res = win(A, B, K)
    sys.stdout.write('Case #%s: %s\n' % (case, res))
