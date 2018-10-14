infile = open('A-small-attempt2.in', 'r')
outfile = open('output-magic.txt', 'w')

t = int(infile.readline())
for i in range(t):
	answer1 = int(infile.readline())
	for j in range(4):
		row = infile.readline()
		if j == answer1-1:
			row1 = row.split(' ')

	answer2 = int(infile.readline())
	for j in range(4):
		row = infile.readline()
		if j == answer2-1:
			row2 = row.split(' ')
	
	count = 0
	for k in range(4):
		for m in range(4):
			if int(row1[k]) == int(row2[m]):
				count += 1
				ans = int(row1[k])

	if count > 1:
		outfile.write("Case #" + str(i+1) + ": Bad magician!\n")
	elif count == 0:
		outfile.write("Case #" + str(i+1) + ": Volunteer cheated!\n")
	else:
		outfile.write("Case #" + str(i+1) + ": " + str(ans) + "\n")
	
