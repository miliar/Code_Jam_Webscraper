import sys

#input
numberOfCases = 0
currentCase = 0

#output
outputLines = []

with open(sys.argv[1]) as inputFile, file("output.txt", 'w') as outputFile:
	for i, line in enumerate(inputFile):
		if i == 0:
			numberOfCases = int(line)
			currentCase = 1
		else:
			audience = line.split(" ")
			currentCase = i
			smax = int(audience[0])
			peopleWithSi = audience[1]
			friendsNeeded = []
			totalPeopleStanding = 0
			friendsNeeded = []
			for i in range (smax, -1, -1):
				totalPeopleStanding = 0

				for k in range (i-1, -1, -1):
					totalPeopleStanding += int(peopleWithSi[k])

				if totalPeopleStanding < i:
					friendsNeeded.append(i - totalPeopleStanding)

			friendsTotal = max(friendsNeeded) if len(friendsNeeded) != 0 else 0
			outputLines.append("Case #{0}: {1}".format(currentCase, friendsTotal))
			if currentCase != numberOfCases: outputLines.append('\n')
	outputFile.writelines(outputLines)