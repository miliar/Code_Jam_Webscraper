#!/usr/bin/python

import sys
import fileinput
import string

input = fileinput.input()

T = int(input.next().strip())

for tcase in xrange(T):
    print 'Case #%d:' % (tcase + 1),
    line = map(int, input.next().split())
    (n, s, p), tots = (line[:3], line[3:])
    cut1 = (p-1) * 3 + 1
    cut2 = max((p-1) * 3 - 1, 1)
    num1 = len([x for x in tots if x >= cut1])
    num2 = len([x for x in tots if x >= cut2 and x < cut1])
    print num1 + min(num2, s)
