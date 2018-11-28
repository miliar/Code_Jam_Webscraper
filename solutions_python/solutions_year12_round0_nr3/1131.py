#!/usr/bin/env python

f = open('C-small-attempt0.in')
out = open('outputS.txt', 'w')

t = int(f.readline())

for i in range(t):
    g = f.readline().split()
    a = int(g[0])
    b = int(g[1])

    c = 0
    for o in range(a, b + 1):
        s = str(o)
        for j in range(1, len(s)):
            k = int(s[j:] + s[:j])
            if a <= o < k <= b:
                c += 1
    out.write('Case #%d: %s\n' % (i + 1, c))
