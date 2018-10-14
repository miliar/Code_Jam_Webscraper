#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

A = ''.join("""ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv""".split())

B = ''.join("""our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up""".split())

M = {}

for x, y in zip(A, B):
    M[x] = y

M['z'] = 'q'

letras = set([chr(x) for x in xrange(ord('a'), ord('z') + 1)])

for x, y in zip(letras - set(M.keys()), letras - set(M.values())):
#    print x, "->", y
    M[x] = y

M[' '] = ' '

#print len(M)
#print len(set(M.values()))

N = int(sys.stdin.readline())
line_num = 1

for line_num in xrange(1, N + 1):
    line = sys.stdin.readline().strip()
    print "Case #%d: " % line_num + ''.join([M[x] for x in line])


