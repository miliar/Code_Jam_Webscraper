import sys,logging

#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

inputFile = open(sys.argv[1])
outFile   = open("outFile.txt", "w")


for caseNum in range(int(inputFile.readline())):
	dimensions = inputFile.readline().split()
	rows  = int(dimensions[0])
	cols  = int(dimensions[1])
	valid = True
	lawn  = []


	maxRowList = []	
	minRowList = []	
	maxColList = []	
	minColList = []	

	for row in range(rows):
		lawn.append(inputFile.readline().rstrip().split())
		maxRowList.append(max(lawn[row]))
		minRowList.append(min(lawn[row]))
		
	for col in range(cols):
		minColList.append(min([row[col] for row in lawn]))
		maxColList.append(max([row[col] for row in lawn]))


	for row in range(rows):
		for col in range(cols):
			value = lawn[row][col]
			if (value < maxRowList[row] and value < maxColList[col]) or int(value) > 100:
				valid = False

	if valid:
		outFile.write("Case #" + str(caseNum+1) + ": YES\n")
	else:
		outFile.write("Case #" + str(caseNum+1) + ": NO\n")
			
