import re, sys

L, D, N = map( int, sys.stdin.readline().split(' ') )

words = []
for i in xrange( D ):
	words += [ sys.stdin.readline()[:-1] ]
for i in xrange( N ):
	query = sys.stdin.readline()[:-1]
	query = re.sub( r"\(([^)]+)\)", r"[\1]", query )
	regx = re.compile( query )

	count = 0
	for w in words:
		if regx.match( w ):
			count += 1
	print "Case #%d: %d" % (i+1, count)
