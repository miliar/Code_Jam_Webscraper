caseAmount = int(input())

for t in range(caseAmount):
	destination, otherHorses = input().split()
	destination = int(destination)
	tempList = []
	totalSpeed = 0
	for z in range(int(otherHorses)):
		initPos, speed = input().split()
		tempList.append([int(initPos), int(speed)])
	for i in range(len(tempList)):
		tempValue = (destination - tempList[i][0]) / tempList[i][1]
		if tempValue > totalSpeed:
			totalSpeed = tempValue
	print("Case #{}: {:0.6f}".format(t+1, destination / totalSpeed))