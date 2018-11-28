import csv
import sys

testCasesNumber	= 0
smallDataSet = True
storeCredit = 0
listItems	= 0

def readTestCases(nCases):
	#print "Number of test cases: " + str(nCases)
	global testCasesNumber
	testCasesNumber = nCases
	if smallDataSet and testCasesNumber<=100:
		print 

def processRow(row1,row2):
	#print row1
	#print row2
	finalCard = []
	for ch in row1:
		if ch in row2:
			#print "Found card " + ch
			finalCard.append(ch)
	if len(finalCard)==1:
		print finalCard[0]
		return finalCard[0]
	elif len(finalCard)>1:
		print "Bad magician!"
		return -1
	elif len(finalCard)==0:
		print "Volunteer cheated!"
		return 0
	else:
		print "Error"


def processElements(answer1,answer2,grid1,grid2):
	#print "*********************"
	#print "Row Answer 1: " + answer1
	#print "Row Answer 2: " + answer2
	#print "Grid1: " +  str(grid1)
	#print "Grid2: " +  str(grid2)
	row = 1
	index = 0
	row1 = []
	row2 = []
	#print "*********************"
	#print "First pass...."
	for item in grid1:
		#print item
		for char in item.split(" "):
			if (int(answer1) == row):
				#print "Adding element:" + char
				row1.append(char)
		row+=1
	row = 1
	index = 0
	#print "Second pass...."
	for item in grid2:
		#print item
		for char in item.split(" "):
			if (int(answer2) == row):
				#print "Adding element:" + char
				row2.append(char)
		row+=1
	processRow(row1,row2)

def readInputFile(fileName):
	lineNumber = 1
	header = ""
	fileReader = csv.reader(open(fileName, 'rb'))
	grid1 = ""
	grid2 = ""
	answer1 = ""
	answer2 = ""
	firstGrid = True
	test = testCasesNumber
	n = 1
	# Read for each Line
	for line in fileReader:
		if (lineNumber == 1 and header == ""):
			header = line
			readTestCases(int(header[0]))
			lineNumber=0
		else:
			try:
				if(firstGrid):
					answer1 = line
					row1 = fileReader.next()
					row2 = fileReader.next()
					row3 = fileReader.next()
					row4 = fileReader.next()
					#print "Answer: " + str(answer1)
					grid1 = row1 + row2 + row3 + row4
					#print grid1
				else:
					answer2 = line
					row1 = fileReader.next()
					row2 = fileReader.next()
					row3 = fileReader.next()
					row4 = fileReader.next()
					#print "Answer 2: " + str(answer2)
					grid2 = row1 + row2 + row3 + row4
					#print grid2
			except Exception, e:
				print "Exception()"	
			lineNumber+=5
			if(lineNumber==5):
				firstGrid = False
			if(lineNumber==10):
				firstGrid = True
				print "Case #" + str(n) + ": ",
				processElements(str(answer1[0]),str(answer2[0]),grid1,grid2)
				lineNumber = 0
				n+=1
		test+=1

		

readInputFile("A-small-attempt0.in")