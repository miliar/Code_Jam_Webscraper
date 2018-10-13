import sys
import string
import time

t0 = time.clock()

try:
	fileInputPointer = open(sys.argv[1], 'r')
	fileOutputPointer = open(sys.argv[2], 'w')
except IOError:
	print("\nInvalid file\n")
	quit()

numberOfCases = int(fileInputPointer.readline().replace('\n',''))
caseNumber = 1
for i in range(0,numberOfCases):
	dimensions = fileInputPointer.readline().replace('\n','').split(' ')
	numberOfRows = int(dimensions[0])
	numberOfColumns = int(dimensions[1])
	rowArray = [[] for i in range(0,numberOfRows)]
	columnArray = [[] for i in range(0,numberOfColumns)]
	lawn = [[100 for i in range(0,numberOfColumns)] for j in range(0,numberOfRows)]
	#lectura de matriz de filas y de columnas
	for row in range(0,numberOfRows):
		readRow = fileInputPointer.readline().replace('\n','').split(' ')
		rowArray[row]=[int(r) for r in readRow]
		for column in range(0,numberOfColumns):
			columnArray[column].append(rowArray[row][column])

	for row in range(0,numberOfRows):
		h = 100 - max(rowArray[row])
		lawn[row][:] = [i-h for i in lawn[row]]

	for column in range(0,numberOfColumns):
		h = 100 - max(columnArray[column])
		for row in range(0,numberOfRows):
			lawn[row][column]=min(lawn[row][column],100-h)
	
	result = True
	for row in range(0,numberOfRows):
		if not (rowArray[row] == lawn[row]):
			result = False
			break
	if (result):
		fileOutputPointer.write('Case #'+str(caseNumber)+": YES\n")
	else:
		fileOutputPointer.write('Case #'+str(caseNumber)+": NO\n")
	caseNumber+=1
			
print("Time: "+str(time.clock()-t0))