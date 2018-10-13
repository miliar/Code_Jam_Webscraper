import sys

def compareSubtract(x,y):
	return x[0] - y[0]

def getOutputName(inputName):
	print inputName.split('.')[0] + ".out"
	return inputName.split('.')[0] + ".out"

def writeAnswer(case, answer, file):
	print "Case #%(tc)d: %(answer)s" % {'tc': case , 'answer':answer}
	file.write("Case #%(tc)d: %(answer)s" % {'tc': case , 'answer':answer})
	file.write("\n")
def writeAnswers(answers, file):
	for i in range(len(answers)):
		writeAnswer(i+1, answers[i], file)

def doTrial(data):
	#implement trial test case here an return the data in a readable format
	checkVar='.'
	isdraw = True
	for col in range(4):
		checkVar = data[0][col]
		if checkVar == '.':
			isdraw = False
			continue
		
		for row in range(1,4):
			if checkVar == 'T':
				checkVar = data[1][col]
				if checkVar == '.':
					break
			if data[row][col] == '.':
				isdraw = False
			if data[row][col] != checkVar and data[row][col] != 'T':
				break
			if row == 3:
				return checkVar + " won"
		if col == 0: #check diagonal
			if checkVar == 'T':
				checkVar = data[1][col+1]
				if checkVar == '.':
					continue
			for row in range(1,4):
				col = col + 1
				if data[row][col] != checkVar and data[row][col] != 'T':
					break
				if row == 3:
					return checkVar + " won"
		if col == 3: #check diagonal
			if checkVar == 'T':
				checkVar = data[1][col+1]
				if checkVar == '.':
					continue
			for row in range(1,4):
				col = col - 1 
				if data[row][col] != checkVar and data[row][col] != 'T':
					break
				if row == 3:
					return checkVar + " won"
	for row in range(4):
		checkVar = data[row][0]
		if checkVar == '.':
			continue
		for col in range(4):
			if data[row][col] != checkVar and data[row][col] != 'T':
				break
			if col == 3:
				return checkVar + " won"
	if isdraw:
		return "Draw"
	return "Game has not completed"
	
if len(sys.argv) > 1:
	fin = file(sys.argv[1])
	fout = file(getOutputName(sys.argv[1]),'w')
	count = 0
	
	numTC = int(fin.readline())
	

	ans = []
	for case in range(numTC):
		data = None
		###### Read in data here from fin, and parse answers.
		data = [fin.readline().rstrip() for x in range(4)]
		fin.readline()
		##### put into some type of readable format.
		##### process the data
		answer = doTrial(data)
		print answer
		ans.append(answer)
	writeAnswers(ans,fout)
	fin.close()
	fout.flush()
	fout.close()