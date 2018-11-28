
with open("A.in", "r") as theFile:
	data = theFile.readlines()

numTerms = int(data[0])

outputList = []
for eachCase in range(numTerms):
	x = int(data[eachCase*10 + 1])
	y = int(data[eachCase*10 + 6])
	test1 = [data[eachCase*10 + 2].split()]
	test1.append(data[eachCase*10 + 3].split())
	test1.append(data[eachCase*10 + 4].split())
	test1.append(data[eachCase*10 + 5].split())
	test2 = [data[eachCase*10 + 7].split()]
	test2.append(data[eachCase*10 + 8].split())
	test2.append(data[eachCase*10 + 9].split())
	test2.append(data[eachCase*10 + 10].split())

	firstGuess = test1[x - 1]
	secondGuess = test2[y - 1]

	ans = 0
	error = 0
	for a in range(4):
		if firstGuess[a] in secondGuess:
			error += 1
			ans = firstGuess[a]

	if error == 0:
		outputList.append("Case #" + str(eachCase + 1) + ": Volunteer cheated!\n")
	if error == 1:
		outputList.append("Case #" + str(eachCase + 1) + ": " + ans + "\n")
	if error > 1:
		outputList.append("Case #" + str(eachCase + 1) + ": Bad magician!\n")


with open("A.out", "w") as outputFile:
	outputFile.writelines(outputList)

