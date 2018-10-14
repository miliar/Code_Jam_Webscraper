import sys

f = open( 'A-large.in', 'r')
test_case = int ( f.readline().rstrip() )

for _ in xrange(1,test_case+1):
	N, M = map( int, f.readline().rstrip().split() )
	pow2 = 2 ** N
	K = M % pow2
	ret = 'OFF'
	if K == pow2 - 1:
		ret = 'ON'
	print 'Case #%d: %s' %(_,ret)
