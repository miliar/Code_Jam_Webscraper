def parseInputFile(name):
	rows = []

	inputFile = open(name, 'r')

	numInputs = int(inputFile.readline())

	for i in range(0, numInputs):
		rows.append(inputFile.readline())

	return rows;

def getSubstitutionTable():
	table = []

	table.append([' ', ' '])
	table.append(['y', 'a'])
	table.append(['', 'b'])
	table.append(['', 'c'])
	table.append(['', 'd'])
	table.append(['', 'e'])
	table.append(['', 'f'])
	table.append(['', 'g'])
	table.append(['', 'h'])
	table.append(['', 'i'])
	table.append(['', 'j'])
	table.append(['', 'k'])
	table.append(['', 'l'])
	table.append(['', 'm'])
	table.append(['', 'n'])
	table.append(['e', 'o'])
	table.append(['', 'p'])
	table.append(['', 'q'])
	table.append(['', 'r'])
	table.append(['', 's'])
	table.append(['', 't'])
	table.append(['', 'u'])
	table.append(['', 'v'])
	table.append(['', 'w'])
	table.append(['', 'x'])
	table.append(['', 'y'])
	table.append(['q', 'z'])

	return table;

def decode(txt, table):
	msg = []

	for i in range(len(txt)):
		for j in range(len(table)):
			if (txt[i] == table[j][0]):
				msg.append(table[j][1])

	return msg

def printTestCase(id, msg):
	print "Case #%d: %s" % (id, ''.join(msg))

def tableContainsLetter(table, letter):
	for i in range(len(table)):
		if table[i][0] == letter:
			return True

	return False

def createTable(inputStr, outputStr, outputTable):
	for i in range(len(inputStr)):
		if tableContainsLetter(outputTable, inputStr[i]) == False:
			outputTable.append([inputStr[i], outputStr[i]])

	return outputTable


inputLines = parseInputFile("A-small-attempt0.in")

outputTable = []

outputTable = createTable("y qee", "a zoo", outputTable)
outputTable = createTable("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand", outputTable)
outputTable = createTable("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities", outputTable)
outputTable = createTable("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up", outputTable)
outputTable = createTable("z", "q", outputTable)

for i in range(len(inputLines)):
	printTestCase(i + 1, decode(inputLines[i], outputTable))
