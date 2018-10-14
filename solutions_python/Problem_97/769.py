#!/usr/bin/python

from sys import stdin

T = int(stdin.readline())
for x in range(1, T + 1):
    A, B = map(int, stdin.readline().split())
    y = 0
    for n in range(A, B):
        s = str(n)
        h = set()
        for i in range(len(s) - 1):
            s = s[1:] + s[:1] # optimize: use int
            m = int(s)
            if n < m <= B and s[0] != '0' and m not in h:
                h.add(m)
                y += 1
    print 'Case #%d: %d' % (x, y)

