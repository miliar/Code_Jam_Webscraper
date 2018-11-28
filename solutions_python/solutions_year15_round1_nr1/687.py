#! /usr/bin/env python3.4
 
def FindMush(numInputs, mList):
	if all(m == mList[0] for m in mList):
		return 0, 0
	
	minA = 0
	for i in range(1, numInputs):
		if mList[i] < mList[i-1]: # M were eaten
			minA += mList[i-1] - mList[i]
	
	minB = 0
	mRate = 0
	# Find the largest rate
	for i in range(1, numInputs):
		diff = mList[i] - mList[i-1]
		if diff < 0 and abs(diff) > mRate:
			mRate = abs(diff)
	
	for i in range(0, numInputs-1):
		minB += min(mRate, mList[i])

	return minA, minB
# Start
file = open("A-large.in")
T = int(file.readline())
outputFile = open("A_Large.txt", 'w')
for i in range(T):
	numInputs = int(file.readline())
	mList = [int(i) for i in file.readline().split()]
	minA, minB = FindMush(numInputs, mList)
	print("Case #{0}: {1} {2}".format(i+1, minA, minB))
	#outputFile.write("Case #{0}: {1} {2} {3}\n".format(i+1, minA, minB, mList))
	outputFile.write("Case #{0}: {1} {2}\n".format(i+1, minA, minB))