import sys

with open( sys.argv[1] ) as dataFile:
    currentCase = 1
    numCases = dataFile.readline()
    for unsplitLine in dataFile:
        A, B = [ int( i ) for i in unsplitLine.split() ]
        count = 0
        for n in range( A, B ):
            m = {}
            nAsList = [ digit for digit in str( n ) ]
            for j in range( 1, len( nAsList ) ):
                mAsStr = ''.join( list( nAsList[j:] ) + list( nAsList[:j] ) )
                if mAsStr[0] != '0' and int( mAsStr ) > n and int( mAsStr ) <= B and mAsStr not in m:
                    count += 1
                m[ mAsStr ] = 0
        print "Case #%s: %s" % ( currentCase, count )
        currentCase += 1

