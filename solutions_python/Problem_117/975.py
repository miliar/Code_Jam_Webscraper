import string 

def canMowLawn(horizontalView, N, M):
	if N == 1 or M == 1: return 'YES'
	verticalView = [list(elem) for elem in zip(*horizontalView)]
	for i in range(0, len(horizontalView)):
		for j in range(0, len(horizontalView[i])):
			elem = horizontalView[i][j]
			if elem != max(horizontalView[i]) and elem != max(verticalView[j]):
				return 'NO'
	return 'YES'

outputList = []
with open('B-large.in') as f:
	listFile = f.readlines()
	noOfCases = int(listFile[0])
	N = 0
	index = 0
	for i in range(1, noOfCases + 1):
		index = index + N + 1 
		matrixSize = listFile[index].split()
		N = int(matrixSize[0])
		M = int(matrixSize[1])
		#print "lenOfVec : " + str(lenOfVec)
		#print [int(elem) for elem in listFile[index + 2].split()]
		matrix = [elem.split() for elem in listFile[index+1:index+N+1]]
		matrix = [map(int, elem) for elem in matrix]
		#print matrix
		outputList.append([i, canMowLawn(matrix, N, M)])
outputFile = open('outputlarge', 'w')
for elem in outputList:
	outputFile.write('Case #' + str(elem[0]) + ": " + str(elem[1]) + "\n")
