#!/usr/bin/python2
# coding: utf-8

from sys import stdin
from copy import deepcopy

T = int(stdin.readline().rstrip())

for ct in range(T):
    _ = int(stdin.readline().rstrip())

    a = sorted(map(float, stdin.readline().rstrip().split()))
    b = sorted(map(float, stdin.readline().rstrip().split()))
    bc = deepcopy(b)

    ur = 0
    for x in a:
        if x < bc[0]:
            bc = bc[:-1]
        else:
            bc = bc[1:]
            ur += 1

    fr = 0
    for x in reversed(a):
        if x > b[-1]:
            b = b[1:]
            fr += 1
        else:
            for i, y in enumerate(b):
                if y > x:
                    b.pop(i)
                    break

    print 'Case #{0}: {1} {2}'.format(ct + 1, ur, fr)
