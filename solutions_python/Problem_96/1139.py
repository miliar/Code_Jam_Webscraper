#!/usr/bin/env python

f = open('B-large.in')
out = open('outputS.txt', 'w')

t = int(f.readline())

for i in range(t):
    g = f.readline().split()
    n = int(g[0])
    s = int(g[1])
    p = int(g[2])
    y = 0
    for j in g[3:]:
        t = int(j)
        if t == 0:
            if p == 0:
                y += 1
            continue
        d = t / 3
        m = t % 3
        if m == 0:
            if d >= p:
                y += 1
            elif d + 1 >= p and s > 0:
                s -= 1
                y += 1
        elif m == 1:
            if d + 1 >= p:
                y += 1
        elif m == 2:
            if d + 1 >= p:
                y += 1
            elif d + 2 >= p and s > 0:
                s -= 1
                y += 1
    out.write('Case #%d: %s\n' % (i + 1, y))

"""
15: 5 5 5; 4 5 6
16: 5 5 6; 4 6 6
17: 5 6 6; 5 5 7
"""
