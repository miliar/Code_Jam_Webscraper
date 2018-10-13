import sys

k = int(sys.stdin.readline())
for t in xrange(k):
	C, F, X = map(float, sys.stdin.readline().split())
	prod = 2.0
	time = 0.0
	while True:
		if X * F < C * (prod + F):
			time += X / prod
			break
		else:
			time += C / prod
			prod += F
	print 'Case #%d: %.7lf' % (t+1, time)