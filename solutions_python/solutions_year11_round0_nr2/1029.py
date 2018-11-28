#!/usr/bin/env python
# -*- coding:Utf-8 -*-

with open( "B-small-attempt0.in", "rt" ) as fileInput :
	with open( "output.txt", "wt" ) as fileOutput :
		t = int( fileInput.readline() )
		for k in range( 1, t + 1 ):
			combineList = {}
			opposedList = {}
			baseList    = []
			line        = ( fileInput.readline() ).split( " " )
			i           = 0
			# Read combine elmts
			c  = int( line [ i ] )
			i += 1
			for j in range( c ):
				combineList[ "%c%c" %( line[ i ][ 0 ], line[ i ][ 1 ] ) ] = line[ i ][ 2 ]
				combineList[ "%c%c" %( line[ i ][ 1 ], line[ i ][ 0 ] ) ] = line[ i ][ 2 ]
				i += 1
			# Read opposed elmts
			d = int( line [ i ] )
			i += 1
			for j in range( d ):
				opposedList[ line[ i ][ 0 ] ] = line[ i ][ 1 ]
				opposedList[ line[ i ][ 1 ] ] = line[ i ][ 0 ]
				i += 1
			# Read elmts
			n = int( line[ i ] )
			i += 1
			elmts = line[ i ].replace( "\n", "" )
			
			# Combine all elmts
			for j in range( n ):
				baseList.append( elmts[ j ] )
				# Combine
				if( len( baseList ) >= 2 ):
					lastElmts = "%c%c" %( baseList[ -1 ], baseList[ -2 ] )
					if( combineList.has_key( lastElmts ) ):
						del baseList[ -2 : ]
						baseList.append( combineList[ lastElmts ] )
				# Opposed
				if( opposedList.has_key( baseList[ -1 ] ) ):
					if( opposedList[ baseList[ -1 ] ] in baseList ):
						del baseList[ : ]
			
			# Write result
			fileOutput.write( "Case #%d: [%s]\n" %( k, ", ".join( baseList ) ) )
