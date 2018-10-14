# Google CodeJam 2011; Round 1; Square Tiles

f = open('A-large.in', 'r')
out = open('output.txt', 'w')
cases = int(f.readline())

for i in range(1, cases + 1):
	output = [""]
	currentLine = f.readline()
	while '.' in currentLine or '#' in currentLine or currentLine == "":
		currentLine = f.readline()
	partitioned = currentLine.partition(' ')
	numRows = int(partitioned[0])
	numCols = int(partitioned[2])
	
#	while 1:
#		try:
#			numRows = int(currentLine[0])
#			numCols = int(currentLine[2])
#		except:
#			currentLine = f.readline()
#		break
	
	currentLine = list(f.readline())
	if numRows > 1:
		nextLine = list(f.readline())
		for x in range(0, numRows):
			if output[0] == "Impossible":
				break
			for y in range(0, numCols):
				if currentLine[y] == '#':
					if y == numCols - 1 or x == numRows - 1:
						output = ["Impossible"]
						break
					elif (not currentLine[y + 1] == nextLine[y] == nextLine[y + 1] == '#'):
						output = ["Impossible"]
						break
					else:
						currentLine[y] = '/'
						currentLine[y + 1] = r'\\'
						nextLine[y] = '\\'
						nextLine[y + 1] = '/'
			if output[0] == "Impossible":
				break
			elif output[0] == "":
				output = [currentLine]
			else:
				output.append(currentLine)
			if x == numRows - 2:
				if '#' in nextLine:
					output = ["Impossible"]
				else:
					output.append("%s" % nextLine)
				break
			else:
				currentLine = nextLine
				nextLine = list(f.readline())
	else:
		if '#' in currentLine:
			output = ["Impossible"]
		else:
			output = [currentLine]
	out.write("Case #%d:\n" % i)
	for x in range(0, len(output)):
		out.write("%s\n" % str(output[x]).replace('[', "").replace('\'', "").replace(']', "").replace(',', "").replace(' ', "").replace('\\\\', '\\').replace('\\n', "").replace('\\\\', '\\'))