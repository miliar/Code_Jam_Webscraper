#!/bin/python
#
# Watersheds

# Run this program with the path to the input file as its only parameter.
# It prints the expected output to the console.
# I used Python 2.5.2 to run it.
#
# Example command line: python watersheds.py input_file.in
import sys

if len( sys.argv ) < 2:
    print "Please supply an input file as a command-line argument."

fp = open( sys.argv[1], 'rb' )

T = int( fp.readline() )

for case in xrange( T ):
    H, W = map( int, fp.readline().split() )
    cells = []
    ds = []
    for row in xrange( H ):
        cells.append( map( float, fp.readline().split() ) )
        ds.append( [ None for x in xrange( W ) ] )
    
    # Now determine where the water flows...
    dirs = (
        ( 0, -1 ),
        ( -1, 0 ),
        ( 1, 0 ),
        ( 0, 1 )
    )
    for row in xrange( H ):
        for col in xrange( W ):
            alt = cells[ row ][ col ]
            target = None
            for d in dirs:
                r = row + d[1]
                c = col + d[0]
                if r < 0 or r >= H or c < 0 or c >= W:
                    continue
                a = cells[ r ][ c ]
                if alt > a:
                    alt = a
                    target = ( r, c )
            ds[ row ][ col ] = target
                        
    # Alrighty.  Iterate over ds and name the cells.
    letterCode = ord('a')
    print "Case #%d:" % ( case + 1, )
    for row in xrange( H ):
        for col in xrange( W ):
            # Find the master target
            r, c = row, col
            while type( ds[ r ][ c ] ) is tuple:
                target = ds[ r ][ c ]
                r, c = target
                
            # See if it has a letterCode assigned
            if ( ds[ r ][ c ] is None ):
                letter = chr( letterCode )
                letterCode += 1
                ds[ r ][ c ] = letter
            else:
                letter = ds[ r ][ c ]
            ds[ row ][ col ] = letter
            
        # Output this row
        print ' '.join( map( str, ds[ row ] ) )