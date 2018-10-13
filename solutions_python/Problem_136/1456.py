#Google Code Jam: Qualification Round - B. Cookie Clicker Alpha

inputfile = open('B-large.in')
outputfile = open('output.txt', 'w')
currentCase = []
cookieData = []
caseIndex = 0
totalTime = 0
currentTime = 0
caseNum = 1
numCases = int(inputfile.readline())

#Build the data list
for line in inputfile:
	currentLine = line.strip().split(' ')
	for num in currentLine:
		currentCase.append(float(num))
	cookieData.append(currentCase)
	currentCase = []

#Determine Possible Solution
while caseIndex < numCases:
	cookieRate = 2
	totalTime = 0
	cost = float(cookieData[caseIndex][0])
	farmRate = float(cookieData[caseIndex][1])
	cookieGoal = float(cookieData[caseIndex][2])
	currentTime = float(cookieGoal/cookieRate)
	nextFarmTime = float(float(cost/cookieRate) + float(cookieGoal/float(cookieRate+farmRate)))

	if currentTime <= nextFarmTime:
		solution = format(float(cookieGoal/cookieRate), '.7f')
		outputfile.write('Case #' + str(caseNum) + ': ' + str(solution) + '\n')
	else:
		totalTime += float(cost/cookieRate)
		while nextFarmTime <= currentTime:
			cookieRate += farmRate
			currentTime = float(cookieGoal/cookieRate)
			nextFarmTime = float(float(cost/cookieRate) + float(cookieGoal/float(cookieRate+farmRate)))
			if nextFarmTime <= currentTime:
				totalTime += float(cost/cookieRate)
		totalTime += currentTime
		solution = format(float(totalTime), '.7f')
		outputfile.write('Case #' + str(caseNum) + ': ' + str(solution) + '\n')
	caseIndex += 1
	caseNum += 1