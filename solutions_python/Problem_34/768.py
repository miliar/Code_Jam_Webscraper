#!/usr/bin/env python

import sys, re, random

class AlienLanguageSolver( object ):
	def __init__( self, filename ):
		self.filename = filename
		self.tests = []
		self.words = []
		self.wordLen = 0

	def readInput( self ):
		lines = map( lambda l: l.strip(), open( self.filename ).readlines() )

		L, D, N = map( lambda s: int(s), lines[0].split() )

		self.words = lines[1:D+1]
		self.tests = lines[D+1:]
		self.wordLen = L
	
	def solve( self ):
		print >>sys.stderr, "Solving..."

		progs = []

		for test in self.tests:
			progs.append( re.compile( test.replace("(","[").replace(")","]") ) )

		test = 1

		for prog in progs:
			count = 0

			for word in self.words:
				if prog.match( word ):
					count += 1

			print "Case #%d: %d" % ( test, count )

			test += 1
	
	def generator( self ):
		print >>sys.stderr, "Generating..."

		L = 15
		L2 = 15
		D = 5000
		N = 500

		alphabet = "".join( [ chr( ord('a') + j ) for j in xrange( L2 ) ])

		for i in xrange( D ):
			self.words.append( "".join([ chr( random.randint( 0, L2 ) + ord('a') ) for j in xrange( L ) ]) )

		for i in xrange( N ):
			pattern = []

			for j in xrange( L ):
				if random.random() > 0.5:
					pattern.append( "(%s)" % "".join( random.sample( alphabet, random.randint( 2, L2 ) ) ) )
				else:
					pattern.append( random.choice( alphabet ) )

			self.tests.append( "".join( pattern ) )

		self.wordLen = L

		for word in self.words:
			print >>sys.stderr, word

		for test in self.tests:
			print >>sys.stderr, test

if __name__ == "__main__":
	random.seed()

	als = AlienLanguageSolver( sys.argv[1] )
	#als.generator()
	als.readInput()
	als.solve()
