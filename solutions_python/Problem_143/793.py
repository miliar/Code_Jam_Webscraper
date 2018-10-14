
import codecs, random

i = 1
for line in codecs.open('input-small.in','r','utf-8').readlines()[1:]:
	A, B, K = map( int, line.split() )

	n = 0
	for a in xrange( A ):
		for b in xrange( B ):
			if a & b < K:
				n += 1

	print 'Case #%d: %d' % ( i, n )
	i += 1
