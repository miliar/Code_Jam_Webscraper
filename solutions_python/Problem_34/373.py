#!/usr/bin/env python

import sys
import re

f = sys.stdin
l, d, n = [int(x) for x in f.readline().strip().split()]
words = []
for i in range(d):
    words.append(f.readline().strip())
for i in range(n):
    print 'Case #%i:' % (i + 1),
    case = f.readline().strip()
    case = case.replace('(', '[').replace(')', ']')
    case = re.compile('^%s$' % case)
    print sum(1 for w in words if case.match(w))
