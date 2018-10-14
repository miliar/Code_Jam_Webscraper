from sys import stdin
from math import sqrt

def answer(arg):
	l,p,c = arg

	ret = 0
	while c * l < p:
		c *= c
		ret += 1
	
	return ret

def case(it):
	while 1:
		yield map(int, it.next().split())

stdin.next()
for cn,d in enumerate(case(stdin)):
	print "Case #%d: %d" % (cn+1, answer(d))
