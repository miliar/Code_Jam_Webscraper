infile = open('small.in', 'r')
outfile = open('small.out', 'w')

# First number is number of test cases, get it first:
fileLines = infile.read().split("\n")
nTestCases = fileLines[0].strip()

lineNum = 1

for case in range(0, int(nTestCases)):
	# Specific test case...
	# First is column from which user got thing.
	pick = [0, 0]
	layout = [[], []]
	pick[0] = int(fileLines[lineNum])
	print "Player picked column", fileLines[lineNum]
	lineNum += 1

	# Layout the layout the magician used.
	layout[0] = []
	layout[0].append(fileLines[lineNum].split(" "))
	layout[0].append(fileLines[lineNum+1].split(" "))
	layout[0].append(fileLines[lineNum+2].split(" "))
	layout[0].append(fileLines[lineNum+3].split(" "))
	lineNum += 4

	pick[1] = int(fileLines[lineNum])
	lineNum += 1
	print "Next pick:", pick[1]

	# Second layout...
	layout[1] = []
	layout[1].append(fileLines[lineNum].split(" "))
	layout[1].append(fileLines[lineNum+1].split(" "))
	layout[1].append(fileLines[lineNum+2].split(" "))
	layout[1].append(fileLines[lineNum+3].split(" "))
	lineNum += 4

	# Load in values from the first pick...
	firstVals = []
	secondVals = []
	for i in range(0, 4):
		firstVals.append(int(layout[0][pick[0]-1][i]))
		secondVals.append(int(layout[1][pick[1]-1][i]))
	print "Possible first values:",firstVals
	print "Possible second values:", secondVals

	# Now, find all possible results:
	possible = []
	for first in firstVals:
		for second in secondVals:
			if first == second:
				possible.append(first)

	# Output:
	if len(possible) == 0:
		outfile.write("Case #" + str(case+1) + ": Volunteer cheated!\n")
	elif len(possible) == 1:
		outfile.write("Case #" + str(case+1) + ": " + str(possible[0]) + "\n")
	else:
		outfile.write("Case #" + str(case+1) + ": Bad magician!\n")