#!/usr/bin/env python
import sys

inp = open(sys.argv[1], 'r')
out = open('outd.txt', 'w')
cases = inp.readline()
for i in range(int(cases)):
    a, b, k = [int(x) for x in inp.readline().split()]
    ands = []
    for j in range(a):
        for l in range(b):
            ands.append(j&l)
    ans = sum(x < k for x in ands)
    print(ans)
    out.write('Case #' + str(i + 1) + ': ' +str(ans) + '\n')
