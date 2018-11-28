#/usr/bin/env python
# -*- coding: utf-8 -*-

import re

line = raw_input().strip().split()
l = int(line[0])
d = int(line[1])
n = int(line[2])
alien = []
for i in range(d):
    alien.append(raw_input())

for i in range(n):
    pat = raw_input().replace('(','[').replace(')',']')
    reg = re.compile(pat)
    res = 0
    for j in range(d):
        if reg.match(alien[j]):
            res = res+1
    print 'Case #%d: %d'%(i+1,res)
