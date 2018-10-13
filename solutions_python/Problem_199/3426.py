#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('A-large.in','r') as f: lines = f.read().splitlines()
d, cn = {'-':'+', '+':'-'}, 1
for x in lines[1:]:
    st,k = x.split()
    s = list(st)
    cnt = 0
    try:
        for i,j in enumerate(s):
            if j=='-':
                cnt +=1
                for m in range(int(k)):
                    s[i+m] = d[s[i+m]]
        print 'Case #{}: {}'.format(cn, cnt)
    except IndexError: print 'Case #{}: {}'.format(cn,'IMPOSSIBLE')
    cn += 1