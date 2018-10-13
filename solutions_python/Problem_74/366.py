#!/usr/bin/env python2.6

import sys, math
import fractions
from itertools import repeat, count, cycle, ifilter, ifilterfalse, \
					  imap, starmap, tee, izip, product, combinations, \
					  permutations
from collections import defaultdict, namedtuple
from operator import itemgetter


def mapInstance( foo, istream ):
	line = istream.readline().split()
	idata = zip(line[1::2], map(int, line[2::2]))
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

Robot = namedtuple('Robot', ('pos', 'time', 'lastpress'))
def solve( idata ):
	robots = {'O': Robot(1, 1, -1), 'B': Robot(1, 1, -1)}

	prev = robots['O'] # does not matter
	for col, pos in idata:
		robot = robots[col]
		dist = abs(robot.pos - pos)
		# move to button
		#print robot.time, ':', col, 'moves to', pos, 'in', dist, 's -> until', robot.time+dist
		robot = robot._replace(pos=pos, time=robot.time+dist)
		# wait to press the button and then press
		t = max(robot.time, prev.lastpress+1)
		#print '    wait until', t, 'to press'
		robot = robot._replace(time=t+1, lastpress=t)

		prev = robot
		robots[col] = robot

	return str(max(robots['O'].time, robots['B'].time)-1)


def main( args ):
	mapInput( solve )

if __name__ == "__main__":
	main( sys.argv )
