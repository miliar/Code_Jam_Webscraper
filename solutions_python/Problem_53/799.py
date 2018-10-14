import sys
import os
import math

basePath = "C:\\Documents and Settings\\thecodedemon\\My Documents\\My Dropbox\\MyFun\\GCJ\\GCJ2010\\1100506_Qualifying\\Snappers\\"

# first read our input file
## inFile = open( basePath + "test.in", 'r' )
## inFile = open( basePath + "A-small-attempt0.in", 'r' )
inFile = open( basePath + "A-large.in", 'r' )

first = True
units = []
snaps = []
for line in inFile:

    line = line.replace( "\n", "" )
    
    if first:
        numLines = int( line )
        first = False

    else:
        units.append( int( line.split( " " )[ 0 ] ) )
        snaps.append( int( line.split( " " )[ 1 ] ) )
inFile.close()

# got the data, now process it
# they will proceed as binary, and we want 2^n - 1 to end up with the light on
# so check if K mod 2^n = -1 = 2^n - 1

i = 0
## outFile = open( basePath + "test.out", 'w' )
## outFile = open( basePath + "A-small-attempt0.out", 'w' )
outFile = open( basePath + "A-large.out", 'w' )

while i < len( units ):

    res1 = math.pow( 2.0, units[ i ] )
    res = snaps[ i ] % res1
    
    # ON
    if res == math.pow( 2, units[ i ] ) - 1:
        outFile.write( "Case #" + str( i + 1 ) + ": ON\n" )
        # print "Case #" + str( i ) + ": ON"

    # OFF
    else:
        outFile.write( "Case #" + str( i + 1 ) + ": OFF\n" )
        # print "Case #" + str( i ) + ": OFF"

    i = i + 1

outFile.close()
