#!/usr/bin/python

import sys
import fileinput
import string

input = fileinput.input()

T = int(input.next().strip())

def solve(n, p1, p2):
    p1.sort()
    p2.sort()

    tmp = p1[::-1]

    ans_real = len(p1)
    for v in p2:
        if tmp[-1] < v:
            tmp.pop()
            ans_real -= 1

    ans_lie = 0
    tmpa = p1[::-1]
    tmpb = p2[::-1]
    while tmpa:
        if tmpa[-1] < p2[0]:
            tmpa.pop()
            p2.pop()
        else:
            tmpa.pop()
            p2 = p2[1:]
            ans_lie += 1

    print ans_lie, ans_real


for tcase in xrange(T):
    print 'Case #%d:' % (tcase + 1),

    n = int(input.next().strip())
    naomi = map(float, input.next().split())
    ken = map(float, input.next().split())

    solve(n, naomi, ken)
