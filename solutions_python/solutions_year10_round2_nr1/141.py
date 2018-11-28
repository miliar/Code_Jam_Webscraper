#!/usr/bin/python

t = int(input())

import sys

for test in range(t):
    d = set()
    n, m = map(int, raw_input().strip().split())
    for i in range(n):
        ln = sys.stdin.readline().strip().split('/')[1:]
        path = []
        for dir in ln:
            path.append(dir)
            tp = tuple(path)
            if tp not in d:
                d.add(tp)
    nr = 0
    for i in range(m):
        ln = sys.stdin.readline().strip().split('/')[1:]
        path = []
        for dir in ln:
            path.append(dir)
            tp = tuple(path)
            if tp not in d:
                d.add(tp)
                nr += 1
    print 'Case #{0}: {1}'.format(test+1, nr)

