import sys
import math

infile = open(sys.argv[1])
num = int(infile.readline())
for herp in range(num):
	completed = True
	o = False
	x = False
	board = []
	strings = []
	for j in range(4):
		currentString = infile.readline().strip()
		strings.append(currentString)
		row = list(currentString)
		board.append(row)
		currentString = ""
	for i in range(4):
		for j in range(4):
			currentString += board[j][i]
		strings.append(currentString)
		currentString = ""

	for i in range(4):
		currentString += board[i][i]
	strings.append(currentString)
	currentString = ""

	for i in range(4):
		currentString += board[i][3-i]
	strings.append(currentString)

	infile.readline()

	for each in strings:
		if ("." not in each and "O" not in each):
			x = True
		if ("." not in each and "X" not in each):
			o = True
		if (".") in each:
			completed = False
	index = str(herp + 1)
	if o:
		print "Case #" + index + ": O won"
	if x: 
		print "Case #" + index + ": X won"
	if not o and not x and not completed:
		print "Case #" + index + ": Game has not completed"

	if not o and not x and completed:
		print "Case #" + index + ": Draw"

