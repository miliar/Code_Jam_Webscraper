from sys import stdin
from itertools import *

def answer(arg):
	n,w = arg

	return sum((
		sum(( 1 for w2 in w if (w1[0]-w2[0]) * (w1[1]-w2[1]) < 0 ))
		for w1 in w )) / 2

def case(it):
	while 1:
		n = int(it.next())
		w = [ map(int, l.split()) for l in islice(it, n) ]
		yield (n,w)

stdin.next()

for cn,d in enumerate(case(stdin)):
	print "Case #%d: %d" % (cn+1, answer(d))
