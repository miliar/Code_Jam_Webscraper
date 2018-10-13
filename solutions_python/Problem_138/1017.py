lines = open('D-large.in', 'r').read().splitlines()
line = iter(lines)

numCases = int(line.next())

outputFile = open('D-large.out', 'w')

for i in range(numCases):
	lenRow = int(line.next())

	row1 = map(lambda t: float(t), line.next().split(" "))
	row1.sort()
	row2 = map(lambda t: float(t), line.next().split(" "))
	row2.sort()

	numWins = 0
	numWinsCheat = 0

	row1copy = row1[:]
	row2copy = row2[:]

	for j in range(lenRow):
		if row1copy[0] > row2copy[0]:
			numWinsCheat = numWinsCheat + 1
			row2copy = row2copy[1:]
		else:
			row2copy = row2copy[:-1]
		row1copy = row1copy[1:]

	for j in range(lenRow):
		cur = row1[j]
		filteredRow2 = filter(lambda t: t > cur, row2)
		if len(filteredRow2) > 0:
			filteredRow2.sort()
			row2.remove(filteredRow2[0])
		else:
			numWins = numWins + 1
			row2 = row2[1:]
	outputFile.write("Case #" + str(i + 1) + ": " + str(numWinsCheat) + " " + str(numWins) + "\n")