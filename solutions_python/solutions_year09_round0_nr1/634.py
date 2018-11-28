import sys, re

ldn = sys.stdin.readline().strip( '\r\n' ).split();
length = int( ldn[ 0 ] )
lines = int( ldn[ 1 ] )
test_count = int( ldn[ 2 ] )

words = []
tests = []

for i in range( lines ):
	words.append( sys.stdin.readline().strip( '\r\n' ) )

for i in range( test_count ):
	test = sys.stdin.readline().strip( '\r\n' )
	test = test.replace( '(', '[' )
	test = test.replace( ')', ']' )

	tests.append( test )

case = 1

for test in tests:
	match_count = 0

	for word in words:
		result = re.match( test, word )

		if result:
			match_count += 1

	print( 'Case #%d: %d' % ( case, match_count ) )

	case += 1
