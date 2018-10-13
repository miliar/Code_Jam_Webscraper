import sys

T = int( raw_input( ) )
for i in xrange( T ) :
    t = map( int, raw_input( ).split( ) ) # total points of the Googlers
    N = t[ 0 ] # number of Googlers
    S = t[ 1 ] # number of surprising triplets of scores
    p = t[ 2 ] # minimum best result for selection
    t = t[ 3 : ]
    
    r = 0
    
    for s in t :
        if s >= 3 * p - 2 :
            r += 1
        elif s >= 3 * p - 4 and S >= 1 and s >= 2 :
            r += 1
            S -= 1
    
    print 'Case #' + str( i + 1 ) + ': ' + str( r )