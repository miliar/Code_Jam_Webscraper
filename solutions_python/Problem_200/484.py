# -*- coding: utf-8 -*-

from __future__ import print_function, division
import sys
if sys.version > '3':
    from past.builtins import xrange, raw_input
    
f = open('B-large.in', 'r')
out = open('answer.txt', 'w+')

def calc(n):
    
    if n <= 9:
        return n
    left = calc(n // 10)
    v = n % 10
    if left < n // 10:
        return left * 10 + 9
    else:
        u = left % 10
        if u <= v:
            return n
        else:
            return calc(left - 1) * 10 + 9

t = int(f.readline())
for i in xrange(t):
    n = int(f.readline())
    #print(n)
    out.write('Case #' + str(i + 1) + ': ' + str(calc(n)) + '\n')
    #print(calc(n, i))
f.close()
out.close()