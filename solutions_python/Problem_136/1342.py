import sys

filename = sys.argv[1]

sys.stdin = open(filename,'r')
numOfCases = int(raw_input())

for x in range(1, numOfCases+1):
	inputs = raw_input()
	numbers = inputs.split()
	C = float(numbers[0])
	F = float(numbers[1])
	X = float(numbers[2])
	currentRate = 2
	currentTime = 0
	while True:
		#build farm
		timeToReachXDirectly = X/currentRate	
			
		timeToBuildFarm = C/currentRate
		timeToBuildFarmAndReachX = timeToBuildFarm + X/(currentRate+F)
		if timeToReachXDirectly <= timeToBuildFarmAndReachX:
			currentTime += timeToReachXDirectly
			break;
		
		else:
			currentTime += timeToBuildFarm
			currentRate +=F	
	print "Case #" + str(x)+ ": " + str(currentTime)
