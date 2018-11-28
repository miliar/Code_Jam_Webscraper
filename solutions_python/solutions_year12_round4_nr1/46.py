#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def token(f):
	ws = ' \t\n'
	while True:
		c = f.read(1)
		if c not in ws: break
	l = [c]
	while True:
		c = f.read(1)
		if c in ws: break
		l.append(c)
	return ''.join(l)

def rt(): return token(sys.stdin)
def ri(): return int(rt())
def rf(): return float(rt())
INF = 10**16

tests = ri()
for case in xrange(1,tests+1):
	n = ri()
	x = []
	l = []
	minh = []
	for _ in xrange(n):
		x.append(ri())
		l.append(ri())
		minh.append(INF)
	D = ri()
	#print "case", case, n, D
	for i in xrange(n-1,-1,-1):
		minh[i] = D-x[i]
		for j in xrange(i+1,n):
			dx = x[j] - x[i]
			if dx > l[i]: break
			if dx < minh[j]: continue
			minh[i] = min(minh[i], dx)
		if minh[i] > l[i]: minh[i] = INF
		#print "minh[%d] = %d" % (i, minh[i]), x[i]
	print "Case #%d: %s" % (case, "YES" if minh[0] <= x[0] else "NO")
