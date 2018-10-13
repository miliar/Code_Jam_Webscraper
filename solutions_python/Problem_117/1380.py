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

def doTrial(data, N, M):
	#implement trial test case here an return the data in a readable format
	#iterate from 1,1 to n+1 m+1 because of the zero padding
	maxcol = data[0]
	maxrows = [0]
	maxrow = 0
	for row in range(1, N+1):
		maxrow = 0
		for col in range(1,M+1):
			if maxcol[col] <= data[row][col] or maxrow <= data[row][col]:
				if maxcol[col] < data[row][col]:
					maxcol[col] = data[row][col]
				if maxrow < data[row][col]:
					maxrow = data[row][col]
			else: 
				return "NO"
		maxrows.append(maxrow)
		
		
	for row in range(1, N+1):
		maxrow = 0
		for col in range(1,M+1):
			if maxcol[col] > data[row][col] and maxrows[row] > data[row][col]:
				return "NO"
	return "YES"
	
if len(sys.argv) > 1:
	fin = file(sys.argv[1])
	fout = file(getOutputName(sys.argv[1]),'w')
	count = 0
	
	numTC = int(fin.readline())
	

	ans = []
	for case in range(numTC):
		data = []
		###### Read in data here from fin, and parse answers.
		[N, M] = [int(x) for x in fin.readline().split()]
		print N
		print M
		data.append([0 for i in range(M+1)])
		for i in range(N):
			l = [0]
			l.extend([int(n) for n in fin.readline().split()])
			data.append(l)
		print data
		##### put into some type of readable format.
		##### process the data
		answer = doTrial(data,N,M)
		print answer
		ans.append(answer)
	writeAnswers(ans,fout)
	fin.close()
	fout.flush()
	fout.close()