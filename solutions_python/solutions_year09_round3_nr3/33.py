# To run this on an input file called sample.in, use the following
# command line:
#
# python prisoners.py sample.in
#
# The output will appear on the console.  I used Python 2.5.2.
import sys

if len( sys.argv ) < 2:
    print "Please provide input file."
    exit(1)

fp = open( sys.argv[1], 'rb' )
cases = int( fp.readline() )

# Brute-force minimum number of coins

def minCoins( prisoners, release, z ):
    coins = None
    for i in xrange(len(release)):
        x = release.pop(i) - 1
        prisoners[ x ] = 0
        #print "%sReleased %d" % (z, x)
        #print "Prisoners: %s" % prisoners
        j = x - 1
        c = 0
        while j >= 0 and prisoners[ j ] == 1:
            c = c + 1
            j = j - 1
        j = x + 1
        while j < len(prisoners) and prisoners[ j ] == 1:
            c = c + 1
            j = j + 1
        if len(release) > 0:
            c += minCoins( prisoners, release, z + '  ' )
        #print "%sCost: %d" % (z, c)
        release.insert(i,x+1)
        prisoners[ x ] = 1
        if coins is None or coins > c:
            coins = c
    return coins

for case in xrange( cases ):
    P, Q = map( int, fp.readline().split() )
    prisoners = [1 for i in xrange( P )]
    release = map( int, fp.readline().split() )
    c = minCoins( prisoners, release, '' )
    print "Case #%d: %d" % ( case + 1, c )