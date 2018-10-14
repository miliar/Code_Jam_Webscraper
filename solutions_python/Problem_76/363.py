#!/usr/bin/env python2.6

import sys, math
import fractions
from itertools import repeat, count, cycle, ifilter, ifilterfalse, \
					  imap, starmap, tee, izip, product, combinations, \
					  permutations
from collections import defaultdict
from operator import itemgetter


def mapInstance( foo, istream ):
	N = int( istream.readline() )
	idata = map( int, istream.readline().split() )
	return foo( idata )

def mapInput( foo, preproc = None, istream = sys.stdin, ostream = sys.stdout ):
	N = map( int, istream.readline().split() )[0]
	if preproc:
		pass
	odata = starmap( mapInstance, repeat( ( foo, istream ), N ) )
	for i, d in enumerate( odata ):
		print >>sys.stderr, "Case #%d" % ( i+1 )
		print >>ostream, "Case #%d: %s" % ( i+1, d )

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

def add(a, b): return (a|b) & ~(a&b)

def solve( idata ):
	# add keeps only bits appearing once in case of two summands
	# or an odd number of times in case of n summands.
	# add is self inverse!

	# try to fail early:
	# every bit has to appear twice overall
	patsum = reduce(add, idata)
	if patsum != 0:
		return "NO"

	# so now taking any sweet out and give it to patrick solves the task
	# (because add is self inverse)
	# so let's give him the cheapest (poor boy)
	return str(sum(idata)-min(idata))

def main( args ):
	mapInput( solve )

if __name__ == "__main__":
	main( sys.argv )
