#!/usr/bin/python

import sys

testIn = open(sys.argv[1], "r")
testOut = open(sys.argv[2], "w")
nbTests = int(testIn.readline())


for nbTest in range(1,nbTests+1):
	line = testIn.readline()[:-1]
	line = line.split(" ")
	A1 = int(line[0])
	A2 = int(line[1])
	B1 = int(line[2])
	B2 = int(line[3])

	counter = 0
	for A in range(A1,A2+1):
		for B in range(B1,B2+1):
			tmpA = A
			tmpB = B
			tmpA,tmpB = max(tmpA,tmpB), min(tmpA,tmpB)
			currentPlayer = 0
			while tmpA>0 and tmpB>0:
				if (tmpA/tmpB) > 1:
					if currentPlayer == 0:
						counter += 1
					break
				else:
					tmpA,tmpB = tmpB, tmpA%tmpB
					currentPlayer = (currentPlayer+1)%2

	outLine = "Case #"+str(nbTest)+": "+str(counter)
	print outLine
	testOut.write(outLine+"\n")

testIn.close()
testOut.close()
