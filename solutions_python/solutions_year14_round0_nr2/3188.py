#!/usr/bin/python

import os,sys

fn = open(sys.argv[1], 'r')

def solve(c, f, x):
	bf = 2.0
	t = 0.0
	while True:
		t1 = x/bf
		t2 = c/bf + x/(bf + f)

#		print "bf=%f,t=%f,c=%f,f=%f,x=%f,t1=%f,t2=%f" % (bf, t, c, f, x, t1, t2)

		if t1 <= t2:
			return t + t1
		else:
			t += c/bf
			bf += f

for t in range(int(fn.readline())):
	(c, f, x) = map(float, fn.readline().strip().split(' '))

	print "Case #%d: %.7f" % (t+1, solve(c, f, x))
