import re
import sys

L, D, N = ( int( x ) for x in sys.stdin.readline().split() )

words = []
for word in range( D ):
    words.append( sys.stdin.readline().strip() )
words = ' '.join( words )

for n in range( N ):
    test = sys.stdin.readline().strip()
    test = test.replace( '(', '[' ).replace( ')', ']' )
    print 'Case #%i:' % ( n + 1 ), len( re.findall( test, words ) )
