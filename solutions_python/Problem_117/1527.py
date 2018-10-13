#! /usr/bin/env python
import sys
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

def TestHorizontalAccess( lawn, x, y ):
    for xIndex in range( len(lawn[y]) ):
        if lawn[y][xIndex] > lawn[y][x]:
            return False
    return True

def TestVerticalAccess( lawn, x, y ):
    for yIndex in range( len(lawn) ):
        if lawn[yIndex][x] > lawn[y][x]:
            return False
    return True

def Test( counter ):
    param = f.readline().replace( '\n', '' ).split( ' ' )
    N = int(param[0])
    M = int(param[1])
    result = True
    lawn = [];
    for yValue in range( N ):
        lawn.append( f.readline().replace( '\n', '' ).split( ' ' ) )
    
    for yValue in range( N ):
        for xValue in range( M ):
            result &= (TestHorizontalAccess( lawn, xValue, yValue ) | TestVerticalAccess( lawn, xValue, yValue ))
    resultStr = 'NO'
    if result:
        resultStr = 'YES'
    fout.write( 'Case #' + str( counter ) + ': '+ resultStr + '\n' )

# Main
T = int( f.readline() )
    
for counter in range( 1, 1 + T ):
    Test( counter )
    percent = float(counter)/float(T) * 100.0
    print str(percent) + '%'
