#!/usr/bin/env python
from sys import stdin
from itertools import *

def possible(T, C, D, vendor):
	spit = vendor[0][0] - T - D

	for p,v in vendor:
		if spit > p + T:
			return False

		spit = max(spit+D, p - T)
		spit += D * (v-1)

		if spit > p + T:
			return False
	
	return True

def answer(data):
	C,D,rd = data
	D *= 2
	vendor = sorted([ (p*2, v) for p,v in rd ])

	t = 0
	thi = D * (sum(( v for p,v in vendor )) + 1)

	while t != thi:
		tm = (t + thi) / 2
		if possible(tm, C, D, vendor):
			thi = tm
		else:
			t = tm + 1
	
	return float(t) / 2
	

def cases(s):
	while 1:
		C,D = map(int, s.next().split())
		yield (C, D, [ map(int, l.split()) for l in islice(s, C) ])

if __name__ == '__main__':
	stdin.next()
	for n,case in enumerate(cases(stdin)):
		print "Case #%d: %s" % (n+1, answer(case))
