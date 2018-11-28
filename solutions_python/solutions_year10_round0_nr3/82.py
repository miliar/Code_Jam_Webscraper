t = int(raw_input().strip())
t_index = 1
while t_index <= t:
	line = raw_input().strip().split(' ')
	r, k, n = int(line[0]), int(line[1]), int(line[2])
	line = raw_input().strip().split(' ')
	gList = [int(g) for g in line]

	nextGroupDict = dict()
	costGroupDict = dict()

	totalCost = 0

	startIndex = 0
	endIndex = startIndex + 1

	while r > 0 and startIndex not in nextGroupDict:
		seat = gList[startIndex]
		if endIndex == n:
			endIndex = 0
		while endIndex != startIndex and seat + gList[endIndex] <= k:
			seat = seat + gList[endIndex]
			endIndex = endIndex + 1
			if endIndex == n:
				endIndex = 0
		nextGroupDict[startIndex] = endIndex
		costGroupDict[startIndex] = seat
		totalCost = totalCost + seat
		r = r - 1
		startIndex = endIndex
		endIndex = startIndex + 1
	if r > 0:
		loopCost = costGroupDict[startIndex]
		endIndex = nextGroupDict[startIndex]
		loopSize = 1
		while endIndex != startIndex:
			loopCost = loopCost + costGroupDict[endIndex]
			loopSize = loopSize + 1
			endIndex = nextGroupDict[endIndex]
		d, r = divmod(r, loopSize)
		totalCost = totalCost + (d * loopCost)
		while r > 0:
			totalCost = totalCost + costGroupDict[startIndex]
			startIndex = nextGroupDict[startIndex]
			r = r - 1
	
	print "Case #%d: %d" % (t_index, totalCost)

	t_index = t_index + 1

