tests = int(raw_input())
casenum = 1
while tests:
	C, F, X = [float(x) for x in raw_input().split()]
	currTime = X/2
	withCTime = (C/2) + X/(2 + F)
	numC = 2
	while currTime > withCTime:
		currTime = withCTime
		timeforC = 0
		for i in range(numC):
			timeforC += (C/(2 + i*F))
		withCTime = X/(2 + numC*F) + timeforC
		numC += 1
	
	print "Case #" + str(casenum) + ": %.7f" % currTime
	casenum += 1
	tests -= 1