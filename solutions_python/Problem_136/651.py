from sys import stdin

T = int(stdin.readline())

for z in xrange(1, T+1):
	(C, F, X) = (float(x) for x in stdin.readline().split())

	r = 2
	time = 0
	while X / r > (C / r + X / (r + F)):
		time += C / r
		r += F
	time += X / r
	print 'Case #' + str(z) + ': ' + str(time)
