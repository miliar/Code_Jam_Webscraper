import fileinput
import sys

myfile = fileinput.input();
maxlawns = 0
currentlawn = 0

for line in myfile:

	if fileinput.isfirstline():
		maxlawns = int(line.strip())
		continue

	dim = line.strip().split()
	dim[0] = int(dim[0])
	dim[1] = int(dim[1])

	lawn = []
	rowmax = []
	colmax = []
	thatsimpossible = False

	currentlawn += 1;
	sys.stdout.write("Case #"+str(currentlawn)+": ")	
	sys.stdout.flush()

	for rowNum in range(dim[0]):
		rowmax.append(1);
		row = myfile.readline().strip().split()
		lawn.append(row)
		
		for colNum in range(dim[1]):
			value = int(row[colNum])

			if (rowNum == 0):
				colmax.append(1)
			if value > rowmax[rowNum]:
				rowmax[rowNum] = value
			if value > colmax[colNum]:
				colmax[colNum] = value

	for rowNum in range(dim[0]):
		for colNum in range(dim[1]):
			value = int(lawn[rowNum][colNum])
			if value < min(rowmax[rowNum], colmax[colNum]):
				thatsimpossible = True
				break
		if thatsimpossible:
			print "NO"
			break
	else:
		print "YES"

	if maxlawns == currentlawn:
		break
