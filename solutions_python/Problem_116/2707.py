# 01_tictactoetomek.py

# Functions
def findMatch(cases, tProcesses = False):
	#print cases

	if ("OOOO" in cases):
		return "O won"
	if ("XXXX" in cases):
		return "X won"
	else:

		# Check for T
		if (tProcesses):
			if ("...." in cases):
				return "Game has not completed"
			else:
				return "Draw"
		else:
			return processT(cases)

def processT(cases):
	for case in cases:
		if (case.count('T') > 0):
			cases.append(case.replace('T', 'X'))
			cases.append(case.replace('T', 'O'))
	# print ['processT debug :: cases ::', cases]
	return findMatch(cases, True)

def findIter(needle, haystack):
	
	result = []
	cutIndex = 0

	numIter = haystack.count(needle)
	if (numIter > 0):
		for matchNum in range(numIter):
			# print ['findIter debug :: haystack ::', haystack]
			pos = haystack.index(needle)
			result.append(cutIndex + pos)
			haystack = haystack[(pos+1):]
			cutIndex = cutIndex+pos+1

	# print ['findIter debug :: result ::', result]
	return result

def sumBlanks(matrix):
	result = []
	for elem in matrix:
		currentElem = findIter('.', elem)
		# if (currentElem == []):
		# 	return False
		# else:
		result = result + currentElem
	# print ['sumBlanks debug :: ', matrix, result, list(set(result))]
	return (list(set(result)) == [0,1,2,3])

# File read
f = open('./A-small-attempt1.in', 'r')
# f = open('./01input.txt', 'r')
#print f
fileLines = f.readlines()
f.close()
fo = open('./A-small-attempt1.out', 'w')

#print fileLines

cases = int(fileLines[0].strip())

# Rows processing
access = 1
for case in range(cases):
	cols = ['','','','']
	rows = ['','','','']
	dgnl = ['','']
	#dots = ['ZZZZ','ZZZZ']
	for lineNum in range(4):
		currentLine = fileLines[access].strip()
		rows[lineNum] = currentLine
		dgnl[0] = dgnl[0] + currentLine[lineNum]
		dgnl[1] = dgnl[1] + currentLine[3-lineNum]
		for colNum in range(4):
			cols[colNum] = cols[colNum] + currentLine[colNum]
		access = access + 1


	notFinished = sumBlanks(rows) or sumBlanks(cols)
	# print ['sumBlanks(rows)',sumBlanks(rows)]
	# print ['sumBlanks(cols)',sumBlanks(cols)]

	if (notFinished): 
		# out = "Case #" + str(case+1) + ": Game has not completed"
		dgnl.append('....')
	# else: 
	
	out = "Case #" + str(case+1) + ": "+ findMatch(cols + rows + dgnl)

	print out
	fo.write(out + '\n')

	access = access+1


fo.close()