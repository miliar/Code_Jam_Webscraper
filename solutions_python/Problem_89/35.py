#! /usr/bin/env python

from math import log

maxprimo = 1000000
primo = [True]*maxprimo
primi = []
primo[0] = False
primo[1] = False
for i in range(2, maxprimo):
    if primo[i]:
        primi.append(i)
        for j in range(2*i, maxprimo, i):
            primo[j] = False

ntest = input()

for test in range(ntest):
    n = input()
    tot = 1
    for p in primi:
        if p * p > n:
            break
        tot += int(log(n, p)) - 1
    if n == 1:
        tot = 0
    print "Case #%d: %d" % (test+1, tot)