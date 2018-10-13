#! /usr/bin/env python3

from collections import namedtuple

Horse = namedtuple('Horse', ('x', 'speed'))

for test in range(1, int(input()) + 1):
    d, n = (int(x) for x in input().split())
    h = []
    for i in range(n):
        h.append(Horse(*(int(x) for x in input().split())))
    ls = 0.0
    rs = 1e18
    for i in range(228):
        ms = (ls + rs) / 2
        flag = True
        for horse in h:
            if (d - horse.x) / horse.speed > d / ms:
                flag = False
                break
        if flag:
            ls = ms
        else:
            rs = ms
    print('Case #{}: {}'.format(test, '%.6f' % ls))
