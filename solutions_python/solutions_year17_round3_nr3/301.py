import math

def maxProductSmall (arr, numCores, training):
	length = len (arr)
	arr = sorted (arr)
	for i in range (length - 1):
		difference = 1.0*(arr [i+1] - arr [i])*(i+1)
		if (difference > training):
			increment = 1.0*training/(i+1)
			for j in range (i+1):
				arr [j] += increment
			training = 0
			break
		else:
			increment = 1.0*difference/(i+1)
			for j in range (i+1):
				arr [j] += increment
			training -= difference
	maxProduct = 1
	for i in range (numCores):
		maxProduct *= arr [i]
	return maxProduct

fRead = open ("C-small-1-attempt0.in", "r")
fWrite = open ("C-small-1-attempt0.txt", "w")

numTests = int (fRead.readline())

for i in range (numTests):
	coreInfo = fRead.readline()
	numCores, numNeeded = [int (x) for x in coreInfo.split()]
	training = float (fRead.readline())
	cores = [float (x) for x in fRead.readline().split()]
	cores.append (float(1.0))
	maxProduct = maxProductSmall (cores, numCores, training)
	fWrite.write ("Case #" + str (i+1) + ": " + str (maxProduct) + "\n")

fRead.close ()
fWrite.close ()