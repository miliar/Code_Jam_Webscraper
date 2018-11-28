# -*- coding: utf-8 -*-

from __future__ import print_function, division
import sys
if sys.version > '3':
    from past.builtins import xrange, raw_input
    
f = open('A-large.in', 'r')
out = open('answer.txt', 'w+')

def calc(s, k):
    
    #print(s)
    answer = 0
    for i in xrange(0, len(s) - k + 1):
        if s[i]:
            for j in xrange(i, i + k):
                s[j] = 1 - s[j]
            answer += 1
        else:
            continue
    #print(s)
    for i in xrange(len(s) - k + 1, len(s)):
        if s[i]:
            return 'IMPOSSIBLE'
    return str(answer)

t = int(f.readline())
for i in xrange(t):
    line = f.readline().split()
    s = [0 if ch == '+' else 1 for ch in line[0]]
    k = int(line[1])
    out.write('Case #' + str(i + 1) + ': ' + calc(s, k) + '\n')

f.close()
out.close()