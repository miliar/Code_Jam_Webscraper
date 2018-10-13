import string 
from math import sqrt

def fairAndSquare(rangeList):
	A = int(rangeList[0])
	B = int(rangeList[1])
	count = 0
	for i in range(A, B+1) :
		if i%10 in [0, 1, 4, 5, 6, 9]:
			if i == int(str(i)[::-1]):
				root = sqrt(i)
				int_root = int(root)
				if 1.0 == root/int_root and int_root == int(str(int_root)[::-1]):
					count = count + 1
	return count

outputList = []
with open('C-small-attempt0.in') as f:
	listFile = f.readlines()
	noOfCases = int(listFile[0])
	for i in range(1, noOfCases + 1):
		rangeList = listFile[i].split()
		outputList.append([i, fairAndSquare(rangeList)])
outputFile = open('outputsmall', 'w')
for elem in outputList:
	outputFile.write('Case #' + str(elem[0]) + ": " + str(elem[1]) + "\n")
