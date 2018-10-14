#!/usr/bin/python3

import sys

t = int(sys.stdin.readline())

def solve(n, x, s):
    cnt = 0
    s.sort()
    i = 0
    j = n-1
    while i < j:
        if s[i] + s[j] <= x:
            cnt += 1
            i += 1
            j -= 1
        else:
            cnt += 1
            j -= 1
    if i == j:
        cnt += 1
    return cnt

for test_case in range(1, t+1):
    n, x = map(int, sys.stdin.readline().split())
    s = [int(y) for y in sys.stdin.readline().split()]
    print('Case #%d: %d' % (test_case, solve(n, x, s)))