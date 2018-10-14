from sys import stdin
from itertools import *

def search(ch, k, dat):
	key = "".join(repeat(ch, k))
	n = len(dat)

	if any(( key in l for l in dat )):
		return True

	trans = [ "".join(l) for l in zip(*dat) ]
	if any(( key in l for l in trans)):
		return True

	for x in xrange(k-1, n):
		s = "".join([ dat[x-j][n-j-1] for j in xrange(x+1) ])
		if key in s:
			return True
		s = "".join([ dat[x-j][j] for j in xrange(x+1) ])
		if key in s:
			return True

	for x in xrange(n+1-k):
		s = "".join([ dat[x+j][n-j-1] for j in xrange(n-x) ])
		if key in s:
			return True
		s = "".join([ dat[x+j][j] for j in xrange(n-x) ])
		if key in s:
			return True
	
	return False

def answer(arg):
	k,dat = arg
	n = len(dat)
	trimmed = [ d.rstrip().replace('.', '') for d in dat ]
	padded = [ "".join(repeat('.', n-len(d))) + d for d in trimmed ]

	Bwin = search('B', k, padded)
	Rwin = search('R', k, padded)

	if Bwin:
		if Rwin:
			return "Both"
		return "Blue"

	if Rwin:
		return "Red"
	return "Neither"

def case(iter):
	while 1:
		n,k = map(int, iter.next().split())
		dat = list(islice(iter, n))
		yield (k,dat)

stdin.next()
for cn,d in enumerate(case(stdin)):
	print "Case #%d: %s" % (cn+1, answer(d))
