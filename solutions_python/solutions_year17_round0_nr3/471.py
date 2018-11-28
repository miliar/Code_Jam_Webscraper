# -*- coding: utf-8 -*-

from __future__ import print_function, division
import sys
if sys.version > '3':
    from past.builtins import xrange, raw_input
    
f = open('C-large.in', 'r')
out = open('answer.txt', 'w+')

def calc(n, k):
    data = {}
    data[n] = 1
    i = 0    
    while i <= k:
        u = max(data) # find the bath
        cur = data[u]
        i += cur
        
        if i >= k:
            return u
        else:
            min_val = (u - 1) // 2
            max_val = (u - 1) - min_val          
            if min_val in data:
                data[min_val] += cur
            else:
                data[min_val] = cur
            if max_val in data:
                data[max_val] += cur
            else:
                data[max_val] = cur

            data.pop(u)

t = int(f.readline())
for i in xrange(t):
    n, k = (int(ch) for ch in f.readline().split())
    answer = calc(n, k)
    min_val = (answer - 1) // 2
    max_val = answer - 1 - min_val
    out.write('Case #' + str(i + 1) + ': ' + str(max_val) + ' ' +  str(min_val) + '\n')

f.close()
out.close()