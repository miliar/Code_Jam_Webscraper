inputFile = open("cruiseControlIn.txt", "r")
outputFile = open("cruiseControlOut.txt", "w")
testCases = int(inputFile.readline())
for i in range(testCases):
	destination, horseCount = [int(x) for x in inputFile.readline().split()]
	lowest = 10000000000000
	for j in range(horseCount):
		initialPos, speed = [int(x) for x in inputFile.readline().split()]
		mySpeed = (speed * destination) / (destination - initialPos)
		if mySpeed < lowest:
			lowest = mySpeed
	outputFile.write("Case #" + str(i + 1) + ": " + str(lowest) + "\n")