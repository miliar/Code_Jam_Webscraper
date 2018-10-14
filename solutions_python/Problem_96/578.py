#!/usr/bin/env python
from sys import stdout

#fin = open("data/sample.in", 'r')
#fin = open("data/b-sample.in", 'r')
fin = open("data/B-large.in", 'r')
#fout = stdout
fout = open("data/b.out", 'w')


cases = int(fin.readline())
for ci in xrange(cases):
    values = map(int, fin.readline().split())
    n, s, p = values[:3]
    result = 0

    for total in values[3:]:
        d, m = divmod(total, 3)
        #print total, " -> ", d, m, s, '(', p , ')'
        if m > 0: d += 1
        if d == p-1 and s > 0:
            if m == 0 and d > 0:
                s -= 1
                result += 1
            elif m == 2:
                s -= 1
                result += 1
        else:
            if d >= p:
                result += 1


    fout.write("Case #%d: %s\n" % (ci+1, result))

