#!/usr/bin/python
import re


L, D, N = map(int, raw_input().split())

pats = []

for x in range(D):
    pats.append(raw_input().strip())


for x in range(N):
    val = raw_input().strip()
    val = val.replace('(', '[').replace(')', ']')
    ans = len([1 for p in pats if re.match(val, p)])
    print 'Case #%d:' % (x+1), ans

