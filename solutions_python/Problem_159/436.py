text = open("/Users/cameronfranz/Documents/Learning/Projects/Code Jam/2015/Round 1A/A-large.in")
numCases = int(text.readline())


for i in range(numCases):	
	
	numPlates = int(text.readline())
	mushrooms	 = text.readline().split()

	minAnyEat = 0
	biggestDiff = 0
	for j in range(len(mushrooms)-1):
		if(int(mushrooms[j])>int(mushrooms[j+1])):
			minAnyEat += int(mushrooms[j])-int(mushrooms[j+1])
			biggestDiff = max(biggestDiff,int(mushrooms[j])-int(mushrooms[j+1]))
	minRateEat = 0
	
	for j in range(len(mushrooms)-1):
			minRateEat += min(biggestDiff,int(mushrooms[j]))
				
	print "Case #" + str(i+1) + ": " + str(minAnyEat),str(minRateEat)
