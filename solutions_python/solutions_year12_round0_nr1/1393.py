#! /usr/bin/env python
#coding=utf-8

import sys
a = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
b = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'

map = {'y' : 'a', 'e' : 'o', 'q' : 'z', 'z' : 'q'}

for i in xrange(len(a)):
    map[b[i]] = a[i]

f = open(sys.argv[1]).read().splitlines()
for t in xrange(int(f[0])):
    u = t + 1
    str = f[u]
    str2 = ''
    for i in str:
        str2 += map[i]
    print 'Case #%d: %s' % (u, str2)
