# -*- coding: utf-8 -*-

from __future__ import print_function, division
import sys
if sys.version > '3':
    from past.builtins import xrange, raw_input
    
f = open('B-small.in', 'r')
out = open('answer.txt', 'w+')

def calc(r, y, b):
    unicorns = [('R', r), ('Y', y), ('B', b)]
    unicorns.sort(key=lambda x:x[1], reverse=True)
    a, b, c = unicorns
    if b[1] + c[1] < a[1]:
        return "IMPOSSIBLE"
    
    k = (c[1] - (a[1] - b[1])) // 2
    #print(a[1], b[1], c[1], k)
    if (c[1] - (a[1] - b[1])) % 2 == 0:
        answer = (c[0] + a[0]) * (a[1] - b[1] + k) + \
                 (b[0] + c[0]) * k + \
                 (b[0] + a[0]) * (b[1] - k)
    else:
        answer = (c[0] + a[0]) * (a[1] - b[1] + k + 1) + \
                 (b[0] + c[0]) * k + \
                 (b[0] + a[0]) * (b[1] - k - 1) + \
                 b[0]
        
    return answer
    

t = int(f.readline())
for i in xrange(t):
    n, r, o, y, g, b, v = (int(ch) for ch in f.readline().split())
    answer = calc(r, y, b)
    out.write('Case #' + str(i + 1) + ': ' + answer +'\n')

f.close()
out.close()