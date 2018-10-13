#!/usr/bin/env python

import sys

def main():
	if len( sys.argv ) == 1:
		print 'Usage: switches inputfile'
		sys.exit(1)
	
	f = open( sys.argv[1], 'r' )
	lines = f.read().split('\n')[:-1]
	f.close()

	cases = int( lines[0] )
	del lines[0]
	
	for i in xrange( cases ):
		engineCount = int( lines[0] )
		del lines[0]
		engines = lines[:engineCount]
		del lines[:engineCount]
		queryCount = int( lines[0] )
		del lines[0]
		queries = lines[:queryCount]
		del lines[:queryCount]

		print 'Case #%d: %s' % ( i+1, countSwitches( engines, queries ) )


def countSwitches( engines, queries ):
	used = {}
	for engine in engines:
		used[engine] = False
	
	switches = 0
	# Pick a starting search engine
	currentEngine = findLastUnusedEngine( engines, queries )

	for i, query in enumerate( queries ):
		if query == currentEngine:
			switches += 1
			currentEngine = findLastUnusedEngine( engines, queries[i:] )
	
	return switches


def findLastUnusedEngine( engines, queries ):
	used = {}

	for query in queries:
		used[query] = True
		if len( used ) == len( engines ) - 1:
			break

	unused = [engine for engine in engines if engine not in used];
	return unused[0]



if __name__ == '__main__':
	main()

