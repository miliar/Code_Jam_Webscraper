#!/usr/bin/python

import sys

t = int(sys.stdin.readline())
for i in range(1, t + 1):
    ans = set([])
    r1 = int(sys.stdin.readline())
    for r in range(1, 5):
        if r == r1:
            ans = set(sys.stdin.readline().split())
        else:
            sys.stdin.readline()
    r2 = int(sys.stdin.readline())
    for r in range(1, 5):
        if r == r2:
            ans = ans & set(sys.stdin.readline().split())
        else:
            sys.stdin.readline()
    if len(ans) == 1:
        print('Case #%d: %s' %(i, list(ans)[0]))
    elif len(ans) == 0:
        print('Case #%d: %s' %(i, 'Volunteer cheated!'))
    else:
        print('Case #%d: %s' %(i, 'Bad magician!'))
