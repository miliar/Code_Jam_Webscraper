import sys

def isValid( num ):
    num = str( num )
    if len( num ) <= 1:     return True 
    for i in xrange( 1, len( num ) ):
        if num[i - 1] > num[i]:     return False
    return True

def solve( N ):
    N = str( N )
    for pos in xrange( len( N ) - 1, -1, -1 ):
        l = list( N )
        for i in xrange( pos, len( N ) ):   l[i] = '9'
        #print "L = ",l
        while ( int( l[ pos ] ) >= 0 ):
            num = int( ''.join( l ) )
            #print num,int(N)
            if num <= int( N ) and isValid( num ):  return num
            l[ pos ] = str( int( l[pos] ) - 1 )
            #print l
    return 0

for cases in xrange( int( sys.stdin.readline() ) ):
    N = int( sys.stdin.readline() )
    print "Case #%d: %d"%( cases + 1, solve( N ) )
    
