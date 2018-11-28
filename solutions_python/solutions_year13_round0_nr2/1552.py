import sys
import math

f = open(sys.argv[1])
lines = f.readlines()
f.close()

lineNumber = 1
t = int(lines[0])

for tt in range(t):
	result = "YES"
	line = lines[lineNumber]
	lineNumber += 1
	fields = line.split()
	#print(fields)
	(field1, field2) = fields
	numRows = int(field1)
	numCols = int(field2)
	design = []

	for i in range(numRows):
		line = lines[lineNumber]
		fields = line.split()
		design.append(fields)
		lineNumber += 1

	while (True):
		if (numRows <= 1) or (numCols <= 1):
			break
		#print (str(numRows) + " " + str(numCols))

		#find the minmum
		minCell = design[0][0]
		minCellRow = 0
		minCellCol = 0

		for i in range(numRows):
			for j in range(numCols):
				if design[i][j] < minCell:
					minCell = design[i][j]
					minCellRow = i
					minCellCol = j

		#print(" ".join([str(minCell), str(minCellRow), str(minCellCol)]))

		#check if row removeable
		numr = 0;
		rowRemovable = False

		#print(design[minCellRow])

		for i in range(numCols):
			if (design[minCellRow][i] == minCell):
				numr += 1
			else:
				break

		if numr == numCols:
			rowRemovable = True

		#print (rowRemovable)

		#check if column removeable
		numc = 0;
		colRemovable = False

		for i in range(numRows):
			if (design[i][minCellCol] == minCell):
				numc += 1
			else:
				break

		if numc == numRows:
			colRemovable = True

		#print (colRemovable)

		if (not colRemovable) and (not rowRemovable):
			result = "NO"
			break

		if colRemovable:
			for i in range(numRows):
				(design[i]).pop(minCellCol)
			numCols -= 1

		if rowRemovable:
			design.pop(minCellRow)
			numRows -= 1

		#for i in range(numRows):
		#	print(design[i])


	print ("Case #" + str(tt+1) + ": " + result)
