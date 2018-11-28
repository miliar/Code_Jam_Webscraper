#!/usr/bin/python

from sys import argv
input = file( argv[1] )

# define problem vars
n = input.next().strip()	# Number of test cases

# helper functions
def run_test( input ):
	s = int( input.next() )	# Number of search engine for current case
	engines = []

	if s == 0: return 0
	for engine in input:
		engines.append( engine.strip() )
		if len( engines ) == s: break

	q = int( input.next() )	# Number of queries for current case
	queries = []
	switches = 0

	if q == 0: return 0
	for query in input:
		queries.append( query.strip() )
		if len( queries ) == q: break
	
	while len( queries ):
		distance = 0
		try:
			for engine in engines:
				distance = max( distance, queries.index( engine ) )
			queries = queries[distance:]
			switches += 1
		except: break
	return switches

# run tests
for i in range( 1, int(n) + 1 ): 
	print "Case #%s: %s" % ( i, run_test( input ) )

