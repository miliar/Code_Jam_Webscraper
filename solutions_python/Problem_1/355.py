#! /usr/bin/python
import math

f = open( "atest" , "r" )
o = open( "atest_output", "w" )

for case in range( int( f.readline() ) ):

	searchEngines = []
	queries = []
	for se in range( int( f.readline() ) ):
		searchEngines.append( f.readline().strip() )

	for qu in range( int( f.readline() ) ):
		queries.append( f.readline().strip() )

	switches = 0
	engineNamesLeft = searchEngines[:]

	for query in queries:
		if query in engineNamesLeft:
			engineNamesLeft.remove( query )

		if len( engineNamesLeft ) == 0:
			switches += 1 
			engineNamesLeft = searchEngines[:]
			engineNamesLeft.remove( query )
	
	o.write( "Case #" + str( case + 1 ) + ": " + str( switches ) + "\n" )
