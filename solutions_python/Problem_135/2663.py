infile = open("A-small-attempt1.in",'r')
outfile = open("a.out",'w')

numInputs = int(infile.readline())

for i in range(numInputs):
	rowA = int(infile.readline())
	rows = []
	rows.append(infile.readline().split(" "))
	rows[0][3] = rows[0][3][:-1]
	rows.append(infile.readline().split(" "))
	rows[1][3] = rows[1][3][:-1]
	rows.append(infile.readline().split(" "))
	rows[2][3] = rows[2][3][:-1]
	rows.append(infile.readline().split(" "))
	rows[3][3] = rows[3][3][:-1]
	rowA = rows[rowA - 1]
	
	rowB = int(infile.readline())
	rows = []
	rows.append(infile.readline().split(" "))
	rows[0][3] = rows[0][3][:-1]
	rows.append(infile.readline().split(" "))
	rows[1][3] = rows[1][3][:-1]
	rows.append(infile.readline().split(" "))
	rows[2][3] = rows[2][3][:-1]
	rows.append(infile.readline().split(" "))
	rows[3][3] = rows[3][3][:-1]
	rowB = rows[rowB - 1]
	
	found = []
	
	outfile.write("Case #" + str(i + 1) + ": ")
	
	for elementA in rowA:
		for elementB in rowB:
			if elementA == elementB:
				found.append(elementB)
	if len(found) > 1:
		outfile.write("Bad magician!")
	elif len(found) == 1:
		outfile.write(found[0])
	else:
		outfile.write("Volunteer cheated!")
	outfile.write("\n")