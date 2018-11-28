# file: 1.py

import sys

def act(label, pos, pPos, canPush):
	if pos == int(testCaseTerms[pPos]):
		if canPush == 1:
			return 0
		else:
			return 0
	else:
		if pos < int(testCaseTerms[pPos]):
			return 1
		elif pos > int(testCaseTerms[pPos]):
			return -1
		else:
			return 0

testCasesQtd = input()
for i in range(testCasesQtd):
	testCaseTerms = raw_input().split(' ')
	rPos = {"O": 1, "B": 1}
	games = 0
	for j in range(int(testCaseTerms[0])):
		while 1:
			games = games + 1
			currentR = j*2+1
			currentP = currentR+1
			move = act(testCaseTerms[currentR], rPos[testCaseTerms[currentR]], currentP, 1)
			for k in range(int(testCaseTerms[0]) - (j + 1)):
				currentSecondR = currentR + ((k+1)*2)
				currentSecondP = currentSecondR+1
				if testCaseTerms[currentR] != testCaseTerms[currentSecondR]:
					rPos[testCaseTerms[currentSecondR]] += act('B', rPos[testCaseTerms[currentSecondR]], currentSecondP, 0)
					break
			if move == 0:
				break
			else:
				rPos[testCaseTerms[currentR]] += move
	print "Case #" + str(i+1) + ": " + str(games)
