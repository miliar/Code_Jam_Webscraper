#! /usr/bin/env python3.4
 
def FindMin(sMax, pList):
	if sMax == 0:
		return 0
	
	reqCount = 0
	for i in range(1, len(pList)):
		sumLesserP = sum(pList[:i])
		if sumLesserP < i:
			reqCount += 1
			pList[i-1] = 1
	return (reqCount)
	
# Start
file = open("A-large.in")
T = int(file.readline())
outputFile = open("A_Large.txt", 'w')
for i in range(T):
	sMax, pList = file.readline().split()
	pList = [int(i) for i in pList]
	sMax = int(sMax)
	result = FindMin(sMax, pList)
	print("Case #{0}: {1}".format(i+1, result))
	outputFile.write("Case #{0}: {1}\n".format(i+1, result))