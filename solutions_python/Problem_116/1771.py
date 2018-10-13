#!/usr/bin/env python3


def processTestData(data, caseNum):
	#check horizontal win
	winingSetX = set(['X', 'T'])
	winingSetO = set(['O', 'T'])
	drawSet = set(['X', 'O', 'T'])

	#main diagonal
	sD1 = set([data[0][0], data[1][1], data[2][2], data[3][3]])
	#the other diagonal
	sD2 = set([data[0][3], data[1][2], data[2][1], data[3][0]])
	for i in range(4):
		sets = list()
		sH = set()
		sV = set()
		notCompleted = False
		for n in range(4):
			#horizontal set
			sH.add(data[i][n])

			#vertical set
			sV.add(data[n][i])


		sets.extend([sH, sV, sD1, sD2])
		for s in sets:
			if not s.difference(winingSetX):
				print('Case #' + str(caseNum) + ': X won')
				return
			if not s.difference(winingSetO):
				print('Case #' + str(caseNum) + ': O won')
				return
			if ('.' in s):
				notCompleted = True

	if notCompleted:
		print('Case #' + str(caseNum) + ': Game has not completed')
	else:
		print('Case #'+ str(caseNum) + ': Draw')	


if __name__ == "__main__":
	import sys
	filename = sys.argv[1]
	f = open(filename, "r+")
	position = 1;
	testsNum = int(f.readline())
	for case in range(testsNum):
		testData = []
		for i in range(position, position+4):
			row = list(f.readline().rstrip('\n'))
			testData.append(row)
		#skip the new line
		f.readline()

		processTestData(testData, case+1)

