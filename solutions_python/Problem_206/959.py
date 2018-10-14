from __future__ import division
T = int( raw_input())

counter = 1
for i in xrange(T):

	D,N = map( int, raw_input().split())
	max_time = 0
	for j in xrange( N):
		K,S = map( int, raw_input().split())
		time = (D - K) / S
		if time > max_time:
			max_time = time

	speed = D / max_time

	print( "Case #%s: %s" % (counter, speed))
	counter += 1