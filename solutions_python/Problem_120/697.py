import sys
numberOfCases = int(sys.stdin.readline())
for caseNumber in range(1, numberOfCases+1):
	case = [int(i) for i in sys.stdin.readline().split()]
	r = case[0]
	t = case[1]
	paintUsed = 0
	ringsDrawn = 0
	while(True):
		paintNeeded = 2*r + 1 #r*r + 2*r +1 - r*r
		if(paintNeeded + paintUsed <= t):
			paintUsed += paintNeeded
			r = r+2
			ringsDrawn += 1
		else:
			break
	
	sys.stdout.write('Case #' + str(caseNumber) + ': ' + str(ringsDrawn))
	if(caseNumber < numberOfCases):
		sys.stdout.write('\n')

