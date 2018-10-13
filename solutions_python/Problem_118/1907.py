#! /usr/bin/env python
import sys
import math
from operator import itemgetter, attrgetter

# Manage input/output
if len( sys.argv ) < 2:
    print "Usage: program.py [filename]"
    exit( 0 )
filename = sys.argv[1]
fileout = filename.replace( '.in', '.out' )

if filename.find( '.in' ) == -1:
    fileout = fileout + '.out'
f = open( filename, 'r' )
fout = open( fileout, 'w' )

def IsFair( number ):
    aString = str( number )
    reverseString = aString[::-1]
    if aString == reverseString:
        return True
    return False

def Test( counter ):
    param = f.readline().replace( '\n', '' ).split( ' ' )
    A = int(param[0])
    B = int(param[1])
    result = 0
    sqrtA = int( math.floor( math.sqrt( A ) ) )
    sqrtB = int( math.ceil( math.sqrt( B ) ) )
    for sqrtValue in range( sqrtA, sqrtB + 1 ):
        value = sqrtValue * sqrtValue
        if A <= value <= B and IsFair( sqrtValue ) and IsFair( value ):
            result += 1
    fout.write( 'Case #' + str( counter ) + ': '+ str(result) + '\n' )

# Main
T = int( f.readline() )
    
for counter in range( 1, 1 + T ):
    Test( counter )
    percent = float(counter)/float(T) * 100.0
    print str(percent) + '%'
