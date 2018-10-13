# -*- coding: utf-8 -*-

from __future__ import print_function, division
import sys
if sys.version > '3':
    from past.builtins import xrange, raw_input
    
from math import pi
    
f = open('A-large.in', 'r')
out = open('answer.txt', 'w+')

t = int(f.readline())
for i in xrange(t):
    n, m = (int(ch) for ch in f.readline().split())
    pancakes = []
    for j in xrange(n):
        r, h = (int(ch) for ch in f.readline().split())
        pancakes.append((r, h, 2.0 * pi * r * h))
    pancakes.sort(key=lambda x:x[0])
    
    max_syrup = 0.0
    for j in xrange(n):
        r, h, area = pancakes[j][0], pancakes[j][1], pancakes[j][2]
        cur_syrup = pi * r * r + area
        plist = []
        for k in xrange(n):
            if k != j and pancakes[k][0] <= pancakes[j][0]:
                plist.append(pancakes[k][2])
        plist.sort(reverse=True)
        cur_syrup += sum(plist[ : m - 1])
        if cur_syrup > max_syrup:
            max_syrup = cur_syrup    
    #print(pancakes)
            
    out.write('Case #' + str(i + 1) + ': ' + "{:.8f}".format(max_syrup) +'\n')

f.close()
out.close()