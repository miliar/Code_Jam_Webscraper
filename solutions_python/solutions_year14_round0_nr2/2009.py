import sys
input = open(sys.argv[1], 'r')

for x in xrange(int(input.readline().strip())):
	vars = map(float,input.readline().split())
	C = vars[0]
	F = vars[1]
	X = vars[2]
	
	bAs = 2.0
	S = X/bAs
	
	qPpF = C/bAs
	qCmF = X/(bAs + F)

	while (qPpF + qCmF) < S:
		S = qPpF + qCmF
		bAs += F

		qPpF += C/bAs
		qCmF = X/(bAs + F)

	print('Case #%d: %f' % (x+1,S))
input.close()