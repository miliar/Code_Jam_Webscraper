#!/usr/bin/env python

from sys import stdin

numCases = eval(stdin.readline())

for caseCount in range(numCases):
    case = caseCount + 1

    n = int(stdin.readline())
    v1 = [int(x) for x in stdin.readline().split()]
    v2 = [int(x) for x in stdin.readline().split()]

    v1.sort()
    v2.sort()
    v2.reverse()

    sum = 0
    for t1,t2 in zip(v1,v2):
        sum += t1*t2

    print "Case #%s: %s" % (case, sum)
