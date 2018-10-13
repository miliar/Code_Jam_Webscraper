# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from __future__ import print_function, division
import sys
if sys.version > '3':
    from past.builtins import xrange, raw_input
    
f = open('A-large.in', 'r')
out = open('answer.txt', 'w+')

t = int(f.readline())
for i in xrange(t):
    d, n = (int(ch) for ch in f.readline().split())
    ks = []
    for j in xrange(n):
        tmp_k, tmp_s = (int(ch) for ch in f.readline().split())
        ks.append((tmp_k, tmp_s))
    ks.sort(key=lambda x:x[1], reverse=True)
    time = 0
    for j in xrange(n - 1, -1, -1):
        if (ks[j][0] < d) and (d - ks[j][0]) / ks[j][1] > time:
            time = (d - ks[j][0]) / ks[j][1]     
    speed = d / time
    out.write('Case #' + str(i + 1) + ': ' + "{:.6f}".format(speed) +'\n')

f.close()
out.close()