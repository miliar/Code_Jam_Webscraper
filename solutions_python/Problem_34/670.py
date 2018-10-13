#!/usr/bin/env python
import fileinput, re

readline = iter(fileinput.input()).next

L, D, N = [int(w) for w in readline().split()]

words = [readline() for i in range(D)]

for case in range(N):
    pattern = readline().replace('(', '[').replace(')', ']')
    regexp = re.compile(pattern)
    matches = sum(regexp.match(word) is not None
                  for word in words)
    print 'Case #{0}: {1}'.format(case + 1, matches)
