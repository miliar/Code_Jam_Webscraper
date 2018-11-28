import sys

def read_integer():
    return int( sys.stdin.readline() )

def read_words():
    return sys.stdin.readline().split()

def read_integers():
    return [ int( x ) for x in read_words() ]

T = read_integer()
for t in range( T ):
    print 'Case #%i:' % ( t + 1 ),
    line = read_words()
    S_max = line[ 0 ]
    S = [ int( digit ) for digit in line[ 1 ] ]
    friends = 0
    standing = 0
    for index, count in enumerate( S ):
        required = max( 0, index - standing )
        friends += required
        standing += required + count
    print friends
