import sys
input = open(sys.argv[1])
numTestCases = int(input.readline())


for t in range(1,numTestCases+1):
	
	args = input.readline().rstrip().split()

	currentShortestTime = None

	accumulated = 0

	farmPrice = float(args[0])
	cookieIncreaseFromFarm = float(args[1])
	target = float(args[2])
	cookiesPerSecond = 2.0

	while True:				

		timeTaken =target/cookiesPerSecond

		totalTime = timeTaken + accumulated

	
		if currentShortestTime == None:
			currentShortestTime = timeTaken
		elif currentShortestTime >totalTime:
			currentShortestTime = totalTime
		else:
			break;

		buyAFarm = farmPrice/cookiesPerSecond	

		accumulated += buyAFarm

		cookiesPerSecond += cookieIncreaseFromFarm

	print "Case #"+str(t) + ":",round(currentShortestTime,7)


