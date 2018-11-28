#!/usr/bin/env python2.6

import sys, math
import fractions
from itertools import repeat, count, cycle, ifilter, ifilterfalse, \
					  imap, starmap, tee, izip, product, combinations, \
					  permutations
from collections import defaultdict
from operator import itemgetter


def mapInstance( foo, istream ):
	mapping = { '1': 1, '0': 0, '.': -1 }
	N = int( istream.readline() )
	idata = []
	for i in xrange(N):
		idata.append(map(mapping.__getitem__, istream.readline().strip()))
	return foo(idata)

def mapInput( foo, preproc = None, istream = sys.stdin, ostream = sys.stdout ):
	N = map( int, istream.readline().split() )[0]
	if preproc:
		pass
	odata = starmap( mapInstance, repeat( ( foo, istream ), N ) )
	for i, d in enumerate( odata ):
		print >>sys.stderr, "Case #%d" % ( i+1 )
		print >>ostream, "Case #%d:\n%s" % ( i+1, d )

class showfunction:
	def __init__( self, foo ):
		self.foo = foo

	def __call__( self, *args ):
		result = self.foo( *args )
		print >>sys.stderr, args, result
		return result

class cachedfunction:
	def __init__( self, foo ):
		self.foo = foo
		self.cache = {}

	def __call__( self, *args ):
		if args in self.cache:
			return self.cache[args]
		else:
			result = self.cache[args] = self.foo( *args )
			return result

def avg(a):
	a = list(a)
	return sum(a)/float(len(a))

def perc(num, denom):
	if num == 0:
		return 0.0
	else:
		return float(num)/denom

def solve( idata ):
	scores = [ [s for s in line if s >= 0] for line in idata ]
	ops = [ [i for i, s in enumerate(line) if s >= 0] for line in idata ]
	W = map(sum, scores)
	N = map(len, scores)
	OWP = [ avg(perc(W[op]-(1-s), N[op]-1) for op, s in izip(opponents, points))
			for opponents, points in izip(ops, scores) ]
	OOWP = [ avg(OWP[op] for op in opponents)
			for opponents in ops ]
	RPI = [ 0.25 * perc(w,n) + 0.50 * owp + 0.25 * oowp
			for w, n, owp, oowp in izip(W, N, OWP, OOWP) ]
	return '\n'.join('%.10f' % f for f in RPI)

def main( args ):
	mapInput( solve )

if __name__ == "__main__":
	main( sys.argv )

