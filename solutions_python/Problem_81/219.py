#!/usr/bin/env python
# -*- coding:Utf-8 -*-

with open( "A-large.in", "rt" ) as fileInput :
	with open( "output.txt", "wt" ) as fileOutput :
		t = int( fileInput.readline() )
		for i in range( 1, t + 1 ):
			n = int( fileInput.readline() )
			schedule = []
			for j in range( n ):
				games  = fileInput.readline()
				schedule.append( list( games.replace( "\n", "" ) ) )
			wp            = []
			playedGamesnb = []
			for j in range( n ):
				playedGames = [ int( x ) for x in schedule[ j ] if x != "." ]
				wp.append( sum( playedGames ) / float( len( playedGames ) ) )
				playedGamesnb.append( len( playedGames ) )
			owp  = []
			for j in range( n ):
				owpv = 0
				for k in range( n ):
					if( schedule[ j ][ k ] != "." ):
						newline = list( schedule[ k ] )
						newline[ j ] = "."
						playedGames = [ int( x ) for x in newline if x != "." ]
						owpv += sum( playedGames ) / float( len( playedGames ) )
				owp.append( owpv / float( playedGamesnb[ j ] ) )
			oowp = []
			for j in range( n ):
				oowpv = 0
				for k in range( n ):
					if( schedule[ j ][ k ] != "." ):
						oowpv += owp[ k ]
				oowp.append( oowpv / float( playedGamesnb[ j ] ) )
			# Write result
			fileOutput.write( "Case #%d:\n" %( i ) )
			for j in range( n ):
				fileOutput.write( "%f\n" %( 0.25 * wp[ j ] + 0.50 * owp[ j ] + 0.25 * oowp[ j ] ) )
