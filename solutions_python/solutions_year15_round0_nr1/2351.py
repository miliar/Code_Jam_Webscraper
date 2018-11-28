for case in range(1, int(input()) + 1):
	testStr = str(input()).split(" ")[1]
	test = [int(i) for i in testStr]
	
	numSoFar = 0
	numToAdd = 0	
	for index, num in enumerate(test):
		if num > 0:
			if numSoFar <= index:
				numToAdd += index - numSoFar
				numSoFar += index - numSoFar			
		numSoFar += num
	
	print("Case #" + str(case) + ": " + str(numToAdd))
	
		
	
