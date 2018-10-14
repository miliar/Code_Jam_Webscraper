#!/usr/bin/env python

def main():
	import sys, itertools

	sys.stdin.readline()
	casenum = 1
	while True:
		line = sys.stdin.readline().strip()
		if line=='': break
		n, N = map( int, line.split(' ') )
		line = sys.stdin.readline().strip()
		if line=='': raise Exception('line numbering')
		ps = map( float, line.split(' ') )
		
		tps = getPByFirstWrongChar(n, ps)
		#print " ".join(["%s"%x for x in tps]), sum(tps)
		
		expecteds = []
		for nBs in xrange(-1, n+1):
			expecteds.append(getExpectedByBs(n, N, tps, nBs))
		leastExpected = min(expecteds)
		
		print 'Case #%s:' % casenum, leastExpected
		casenum += 1


def getExpectedByBs(n, N, tps, nBs):
	total = 0
	for firstWrongChar in xrange(n+1):
		# print n, firstWrongChar
		keysNeeded = getKeysNeeded(n, N, firstWrongChar, nBs)
		# print n, N, nBs, firstWrongChar, keysNeeded
		total += keysNeeded * tps[firstWrongChar]
	return total

def getP(ps, mask):
	l = len(ps); assert l == len(mask)
	prod = 1.0
	for i in xrange(l):
		p = ps[i]
		if mask[i]: prod *= p
		else: prod *= (1 - p)
	# print ps, mask, prod
	return prod

def getPByFirstWrongChar(n, ps):
	import itertools
	assert n == len(ps)
	pByFirstWrongChar = [0] * n
	pNoWrongChar = 0
	# http://stackoverflow.com/questions/4928297
	for guessTruth in itertools.product([True, False], repeat=n):
		# print guessTruth, n
		firstWrongChar = None
		for i in xrange(len(guessTruth)):
			if guessTruth[i] == False:
				pByFirstWrongChar[i] += getP(ps, guessTruth)
				break
		else: pNoWrongChar += getP(ps, guessTruth)
	return pByFirstWrongChar + [pNoWrongChar]


def getKeysNeeded(n, N, firstWrongChar, nBs):
	assert firstWrongChar >= 0 and firstWrongChar <= n
	if nBs == -1: return 1 + N + 1 # enter, password, enter
	c = nBs * 2 + (N - n) + 1 # backspaces, rest of password, enter
	if n - nBs > firstWrongChar: # wrong password
		c += N + 1 # new password, enter
	return c

if __name__ == '__main__': main()
