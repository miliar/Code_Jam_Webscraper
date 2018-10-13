#!/usr/bin/python

import os, sys, re, math, random


input = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jvzq'''

output = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give upqz'''

T = {}

for x,y in zip(input, output):
    T[x] = y

n = int(raw_input())
for i in range(n):
    s = raw_input()
    t = ''.join(map(lambda x: T[x], s))
    print 'Case #%d: %s' % (i+1, t)

