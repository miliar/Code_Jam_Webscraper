import sys
from math import *
from CIO import *

def check(p, t, n):
	# pancakes per plate / time excluding special minutes / special minutes
	p = [x for x in p if x > t]
	if len(p) == 0:
		return True
	if t == 0:
		return False
	for x in p: 
		n -= int(ceil(1.0 * x / t)) - 1
		if n < 0: 
			return False
	return True

def checkTime(p, t):
	# pancakes per plate / time including special minutes
	for i in range(t+1):
		if check(p, t - i, i):
			return True
	return False

def solve(p):
	lower = 0
	upper = 1
	while not checkTime(p, upper):
		lower = upper
		upper *= 2
	while lower != upper:
		m = (lower + upper) / 2
		if checkTime(p, m):
			upper = m
		else:
			lower = m + 1
	return lower

if __name__ == "__main__":
	fname = sys.argv[1]
	cio = CIO(fname)
	for i in cio.n():
		d = cio.i()
		p = cio.il()
		cio.w(solve(p))
	cio.c()
	

