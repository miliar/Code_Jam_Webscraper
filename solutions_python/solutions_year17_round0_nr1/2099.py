inputFile = open(input("> "), "r")
outputFile = open("pancakeOut.txt", "w")

testCases = int(inputFile.readline())
for i in range(testCases):
	line = inputFile.readline().split()
	statesOri = list(line[0])
	panSize = int(line[1])
	states = []
	for j in statesOri:
		if j == '-':
			states.append(False)
		else:
			states.append(True)
	count = 0
	for j in range(len(states) - panSize + 1):
		if states[j] == False:
			count += 1
			for k in range(j, j + panSize):
				states[k] = not states[k]
	if i < testCases - 1:
		if not False in states:
			outputFile.write("Case #" + str(i + 1) + ": " + str(count) + "\n")
		else:
			outputFile.write("Case #" + str(i + 1) + ": IMPOSSIBLE\n")
	else:
		if not False in states:
			outputFile.write("Case #" + str(i + 1) + ": " + str(count))
		else:
			outputFile.write("Case #" + str(i + 1) + ": IMPOSSIBLE")