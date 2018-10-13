infile = open('input.in', 'r')
outfile = open('output.out','w')
numCases = int(infile.readline())
for case in range(numCases):
	firstRow = int(infile.readline())-1
	table = {}
	for row in range(4):
		table[row] = infile.readline()
	firstRow = table[firstRow].split()

	secondRow = int(infile.readline())-1
	for row in range(4):
		table[row] = infile.readline()
	secondRow = table[secondRow].split()

	badMagician = False
	found = False
	card = None
	for item in firstRow:
		if item in secondRow and not found:
			found = True
			card = int(item)
		elif item in secondRow and found:
			badMagician = True
	if badMagician:
		outfile.write("Case #{0}: Bad magician!\n".format(case+1))
	elif found:
		outfile.write("Case #{0}: {1}\n".format(case+1,card))
	else:
		outfile.write("Case #{0}: Volunteer cheated!\n".format(case+1))

	
