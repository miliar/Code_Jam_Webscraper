inputFile = open('A-small-attempt0.in', 'r')
outputFile = open('A-small-attempt0.out', 'w')
lines = [l for l in inputFile]
testsNo = int(lines[0])
for i in range(testsNo):
	testCaseLine = i * 10 + 1
	possibleNums = []
	for j in range(2):
		roundLine = testCaseLine + j * 5
		rowLine = roundLine + int(lines[roundLine])
		possibleNums += lines[rowLine].strip().split(" ")
	nums = set([n for n in possibleNums if possibleNums.count(n) > 1])
	if (len(nums) == 1):
		result = str(nums.pop())
	elif (len(nums) > 1):
		result = "Bad magician!"
	else:
		result = "Volunteer cheated!"
	outputFile.write("Case #"+str(i+1)+": "+result+"\n")
