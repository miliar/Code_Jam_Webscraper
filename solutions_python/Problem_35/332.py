#!/usr/bin/env python

import numpy as np

import sys
f = sys.stdin

def flows_to(d, x, y):
    l = d[y + 1][x + 1]
    lowest = min(d[y][x + 1], d[y + 1][x], d[y + 1][x + 2], d[y + 2][x + 1])
    if d[y][x + 1] < l and d[y][x + 1] == lowest:
        return (x, y - 1)
    if d[y + 1][x] < l and d[y + 1][x] == lowest:
        return (x - 1, y)
    if d[y + 1][x + 2] < l and d[y + 1][x + 2] == lowest:
        return (x + 1, y)
    if d[y + 2][x + 1] < l and d[y + 2][x + 1] == lowest:
        return (x, y + 1)
    return None

t = int(f.readline().strip())
for i in range(t):
    h, w = [int(x) for x in f.readline().strip().split()]
    d = np.ones((h + 2, w + 2), dtype=int) * 90000
    sheds = [[None] * w for j in range(h)]
    for j in range(h):
        l = f.readline().strip().split()
        for k, v in enumerate(l):
            d[j + 1][k + 1] = v

    for j in range(h):
        for k, v in enumerate(d[h + 1][1:-1]):
            if sheds[j][k] is not None:
                continue
            x, y = k, j
            flow = [(x, y)]
            while True:
                shed = flows_to(d, x, y)
                if shed is None:
                    dest = list()
                    for z in flow:
                        sheds[z[1]][z[0]] = dest
                    break
                elif sheds[shed[1]][shed[0]] is not None:
                    dest = sheds[shed[1]][shed[0]]
                    for z in flow:
                        sheds[z[1]][z[0]] = dest
                    break
                else:
                    flow.append(shed)
                    x, y = shed

    shedl = list('abcdefghijklmnopqrstuvwxyz')
    for j in range(h):
        for k in range(w):
            if not sheds[j][k]:
                sheds[j][k].append(shedl.pop(0))

    print 'Case #%i:' % (i + 1)
    print '\n'.join(' '.join([v[0] for v in line]) for line in sheds)
