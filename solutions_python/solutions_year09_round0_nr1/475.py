#!/usr/bin/python
import re

L, D, N = map(int, raw_input().split())
dicc = ''
for i in range(D):
    dicc += raw_input() + ' '

for i in range(N):
    expr = raw_input()
    expr = expr.replace('(', '[')
    expr = expr.replace(')', ']')
    expr_c = re.compile(expr)
    print 'Case #%s: %s' % (i + 1, len(expr_c.split(dicc)) - 1)
