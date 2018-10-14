lines = open('A-small-attempt0.in', 'r').read().splitlines()
line = iter(lines)

numCases = int(line.next())

outputFile = open('A-small-attempt0.out', 'w')

for i in range(numCases):
	firstRowPicked = int(line.next())
	# firstMatrix
	for j in range(4):
		if firstRowPicked == j + 1:
			firstRow = line.next()
			# print "first row"
			# print firstRow
		else:
			line.next()
			# print line,
	secondRowPicked = int(line.next())
	# secondMatrix
	for j in range(4):
		if secondRowPicked == j + 1:
			secondRow = line.next()
			# print "second row"
			# print secondRow
		else:
			line.next()
	possibleValue = set(firstRow.split(" ")).intersection(set(secondRow.split(" ")))
	if len(possibleValue) == 0:
		outputFile.write("Case #" + str(i + 1) + ": Volunteer cheated!\n")
	elif len(possibleValue) == 1:
		outputFile.write("Case #" + str(i + 1) + ": " +  list(possibleValue)[-1] + "\n")
	else:
		outputFile.write("Case #" + str(i + 1) + ": Bad magician!\n")



