"""
We can do one more optimization: we can use a dictionary with keys all numbers 0..2000000, with values the lists of recycled numbers containing the respective number.
Then, in ComputeNumberRecycledNumbers() we can look only for the lists of recycled numbers referred in this dictionary for values A..B.
    This yields complexity O( (B-A) * 7) (at most 7 recycled numbers per list).
Note that with the current implementation we have O(5748473 * 7), where 5748473 is the total number of precomputed lists of recycled numbers for A=0, B=2000000.
"""

#From https://code.google.com/codejam/contest/1460488/dashboard#s=p2

import sys
import string
import sets

sys.stdout.softspace = 0

MY_DEBUG = False
#MY_DEBUG = True



listLists = []

USE_LIST = True
def GenerateAllRecycledNumbers():
    B = 2000000 #3000 #2000000

    totalLen = 0

    alreadyProcessed = sets.Set([])

    for i in range(B + 1):
    #for i in range(1234, 1235):
    #for i in range(12345, 12346):
	strI = str(i)

	if (USE_LIST):
	    if (i not in alreadyProcessed):
		alreadyProcessed.add(i)
    		listPermutations = [i] #Permute the digits one position at a time, to the left
    	    else:
    		continue
	else:
	    listPermutations = sets.Set([i])

	for pos in range(len(strI) - 1):
	    if (MY_DEBUG):
		print "pos =", pos
	    strI = strI[1:] + strI[0]

	    if (MY_DEBUG):
		print "strI =", strI

	    if (USE_LIST):
		val = int(strI)
		try:
    		    res = listPermutations.index(val)
    		except ValueError:
    		    res = -1

		if (res == -1):
		    if (val not in alreadyProcessed):
            		listPermutations.append(val)
			alreadyProcessed.add(val)
	    else:
                listPermutations.add(int(strI))

	if (MY_DEBUG):
            print "listPermutations =", listPermutations

        totalLen += len(listPermutations)

	listLists.append(listPermutations)

    """
    if (MY_DEBUG):
	print "totalLen =", totalLen
    """
    print "totalLen =", totalLen


def ComputeNumberRecycledNumbers(A, B):
    numRecycledNumbers = 0

    for i in range(len(listLists)):
	numValuesToPair = 0
	for j in range(len(listLists[i])):
    	    if ( (listLists[i][j] >= A) and (listLists[i][j] <= B) ):
		numValuesToPair += 1
		"""
		for k in range(len(listLists[j])):
    		    if ( (listLists[i][k] >= A) and (listLists[i][k] <= B) ):
			numRecycledNumbers += 1
		"""
	if (numValuesToPair >= 2):
	    numRecycledNumbers += numValuesToPair * (numValuesToPair - 1) / 2
	    if (MY_DEBUG):
    		print "numRecycledNumbers = %d, listLists[%d] = %s" % (numRecycledNumbers, i, listLists[i])

    return numRecycledNumbers


def ReadData(fileName):
    f = open(fileName, "rb")

    T = int(f.readline())

    if (MY_DEBUG):
        print "T =", T

    GenerateAllRecycledNumbers()

    for i in range(1, T + 1):
        line = f.readline().rstrip()
	lineList = string.split(line, " ")

	if (MY_DEBUG):
    	    print line

	A = int(lineList[0])
	B = int(lineList[1])
	#print "A = %d, B = %d: ComputeNumberRecycledNumbers(A, B) = %d" % (A, B, ComputeNumberRecycledNumbers(A, B))

	if (MY_DEBUG):
    	    print "A = %d, B = %d" % (A, B)

	num = ComputeNumberRecycledNumbers(A, B)
	#print "Translation: ", lineDecrypted
	print "Case #%d: %d" % (i, num)

    f.close()
    #fOut.close()


#"Training" the mapping
#ReadData("C.in")
#ReadData("C-small-attempt0.in")
ReadData("C-large.in")
