# -*- coding: utf-8 -*-
import re

fin = open("a.in","r")
L, D, N = map(int, fin.readline().split())

words = []
for i in range(D):
    words.append(fin.readline().strip())

for i in range(N):
    pattern = fin.readline().strip()
    pattern = pattern.replace('(', '[').replace(')',']')
    
    p = re.compile(pattern)
    
    count = 0
    for w in words:
        if p.match(w):
            count += 1
    
    print "Case #%d: %d" % (i+1, count)
    
