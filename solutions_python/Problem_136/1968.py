TC = input()
def time(C,F,X,N):
	return sum(C / (2+F*(k-1)) for k in xrange(1,N+1)) + X/(2+F*N)

for tc in xrange(TC):
	C,F,X = (float(a) for a in raw_input().split())
	N = 0
	minimum = X/2.0
	curtimebase = 0.0;
	while True:
		N += 1
		curtimebase += C / (2+F*(N-1))
		test = curtimebase + X/(2+F*N)
		if test < minimum:
			minimum = test
		else:
			break
	print 'Case #%d: %.7f' % (tc+1, minimum)
