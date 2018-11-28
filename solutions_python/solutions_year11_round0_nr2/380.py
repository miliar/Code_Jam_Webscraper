#!/usr/bin/env python2.6

import sys, math
import fractions
from itertools import repeat, count, cycle, ifilter, ifilterfalse, \
					  imap, starmap, tee, izip, product, combinations, \
					  permutations
from collections import defaultdict
from operator import itemgetter


def mapInstance( foo, istream ):
	line = istream.readline().split()
	C = int(line[0])
	reactions = line[1:C+1]
	line = line[C+1:]

	D = int(line[0])
	opposed = line[1:D+1]
	line = line[D+1:]

	sequence = line[1]
	idata = (reactions, opposed, sequence)
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

def solve( idata ):
	reactions, opposed, sequence = idata

	re = {}
	for a, b, c  in reactions:
		src = a+b
		re[src] = c
		src = b+a
		re[src] = c

	op = defaultdict(set)
	for a, b in opposed:
		op[a].add(b)
		op[b].add(a)

	base = set()
	o = ''
	prev = ' '
	for c in sequence:
		src = prev+c
		if src in re:
			o = o[:-1]+re[src]
			prev = ' '
		elif len(op[c] & base) > 0 or prev in op[c]:
			o = ''
			base = set()
			prev = ' '
		else:
			if prev != ' ':
				base.add(prev)
			o += c
			prev = c
	return "[{0}]".format(', '.join(o))

def main( args ):
	mapInput( solve )

if __name__ == "__main__":
	main( sys.argv )
