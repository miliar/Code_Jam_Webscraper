#!/usr/bin/python2.7
import sys

def simulate(c,f,x,n):
	num_farms = 0
	t = 0.0
	while num_farms < n:
		cps = 2.0+num_farms*f
		t += c/cps
		num_farms += 1

	cps = 2.0+num_farms*f
	return t+(x/cps)

def compute(c,f,x):
	prev_t = None
	n = 0
	while True:
		t = simulate(c,f,x,n)
		if prev_t != None and t > prev_t:
			return "{0:.7f}".format(prev_t)
		prev_t = t
		n += 1

lines = sys.stdin.read().splitlines()
num_cases = int(lines.pop(0))

for i in xrange(num_cases):
	c,f,x = map(float, lines.pop(0).split())
	print "Case #{0}: {1}".format(i+1, compute(c,f,x))
