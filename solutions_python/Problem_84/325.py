#!/usr/bin/env python
# -*- coding:Utf-8 -*-

with open( "A-large.in", "rt" ) as fileInput :
	with open( "output.txt", "wt" ) as fileOutput :
		t = int( fileInput.readline() )
		for i in range( 1, t + 1 ):
			r, c = map( int, ( fileInput.readline() ).split( " " ) )
			pic  = []
			for j in range( r ):
				pic.append( list( fileInput.readline().replace( "\n", "" ) ) )
			
			k = 0
			while( k < r ):
				j = 0
				while( j < c ):
					if( pic[ k ][ j ] == "#" ):
						if( j < ( c - 1 ) and k < ( r - 1 ) ):
							if( pic[ k + 1 ][ j ] == "#" and pic[ k ][ j + 1 ] == "#" and pic[ k + 1 ][ j + 1 ] == "#" ):
								pic[ k ][ j ]          = "/"
								pic[ k + 1 ][ j ]      = "\\"
								pic[ k ][ j + 1 ]      = "\\"
								pic[ k + 1 ][ j + 1 ]  = "/"
					j += 1
				k += 1
			# Write result
			fileOutput.write( "Case #%d:\n" %( i ) )
			ok = True
			for j in range( r ):
				if( "#" in pic[ j ] ):
					ok = False
					break
			if( ok ):
				for j in range( r ):
					fileOutput.write( "".join( pic[ j ] ) )
					fileOutput.write( "\n" )
			else:
				fileOutput.write( "Impossible\n" )
