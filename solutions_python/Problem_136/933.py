testCases = int(raw_input())
for test in range(testCases):
	C, F, X = [float(i) for i in raw_input().split(" ")]
	currentTime = 0.0
	currentC = C/2.0
	currentF = 2.0 + F
	bestTime = X/2.0
	while(1):
		if (currentC + (X/currentF)) < bestTime:
			bestTime = (currentC + (X/currentF)) 
			currentC += C/currentF
			currentF += F
		else:
			break
	print "Case #" + str(test+1) + ": " + "%.7f" % bestTime
