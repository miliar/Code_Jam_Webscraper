#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

rl = sys.stdin.readline

t = int(rl())

for c in xrange(0, t) :
	cur = map(int, rl().split())
	L = cur[0]
	P = cur[1]
	C = cur[2]
	
	cnt = 0
	
	while L*C < P:
		cnt = cnt + 1
		C = C**2
	
	print 'Case #%d: %d' % (c+1, cnt)
	
		