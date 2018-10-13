import math     # need math.ceil(), as round() function can't round properly

allocationAmount = int(input())

for t in range(allocationAmount):
	totalStalls, amountOfPeople = input().split()
	totalStalls = int(totalStalls)
	amountOfPeople = int(amountOfPeople)
	currentIndex = 0
	stalls = []
	for i in range(totalStalls):
		stalls.append("a")
	for j in range(amountOfPeople):
		if "o" not in stalls:
			currentIndex = math.ceil(totalStalls / 2) - 1
			stalls[currentIndex] = "o"
		else:
			occupiedIndList = []
			for oInd in range(len(stalls)):
				if stalls[oInd] == "o":
					occupiedIndList.append(oInd)
			gapEndIndList = occupiedIndList + [totalStalls]
			gapList = [occupiedIndList[0]]
			for k in range(1, len(gapEndIndList)):
				gapList.append(gapEndIndList[k] - gapEndIndList[k-1] - 1)
			temp1 = math.ceil(max(gapList)/2)
			temp2 = gapList.index(max(gapList)) - 1
			if temp2 < 0:
				currentIndex = temp1 - 1
			else:
				currentIndex = gapEndIndList[temp2] + temp1
			stalls[currentIndex] = "o"
	tempCountList = []
	# get left side space of last person
	tempIndex = currentIndex - 1
	tempCount = 0
	done = False
	while not done:
		if tempIndex < 0 or stalls[tempIndex] == "o":
			tempCountList.append(tempCount)
			done = True
		else:
			tempCount += 1
			tempIndex -= 1
	# get right side space of last person
	tempIndex = currentIndex + 1
	tempCount = 0
	if tempIndex != len(stalls):
		done = False
		while not done:
			if tempIndex == len(stalls) or stalls[tempIndex] == "o":
				tempCountList.append(tempCount)
				done = True
			else:
				tempCount += 1
				tempIndex += 1

	print("Case #{}: {} {}".format(t+1, max(tempCountList), min(tempCountList)))
