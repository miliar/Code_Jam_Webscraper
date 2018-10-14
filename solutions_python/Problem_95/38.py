#!/usr/bin/env python

tr = {}

def match(a, b):
	for x, y in zip(a, b):
		tr[x] = y

match('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand')
match('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities')
match('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')
match('y qee', 'a zoo')
match('z', 'q')

def translate(a):
	return ''.join([tr[x] for x in a])

import sys
lines = sys.stdin.readlines()
T = int(lines[0])
for i in xrange(1, T + 1):
	print 'Case #%d:' % i, translate(lines[i].strip())