import sys
import math

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

def isPalindrone(num):
	snum = str(num)
	length = len(snum)
	iter = len(snum)/2
	for i in range(iter):
		if snum[i] != snum[length-i-1]:
			return False
	return True

def doTrial(data):
	#implement trial test case here an return the data in a readable format
	[N, M] = data
	max = int(math.floor(math.sqrt(M)))
	min = int(math.ceil(math.sqrt(N)))
	count = 0
	for i in range(min,max+1):
		if	isPalindrone(i) and isPalindrone(i*i):
			count = count +1
	return count
	
if len(sys.argv) > 1:
	fin = file(sys.argv[1])
	fout = file(getOutputName(sys.argv[1]),'w')
	count = 0
	
	numTC = int(fin.readline())
	

	ans = []
	for case in range(numTC):
		data = None
		###### Read in data here from fin, and parse answers.
		data = [int(x) for x in fin.readline().split()]
		
		##### put into some type of readable format.
		##### process the data
		answer = doTrial(data)
		print answer
		ans.append(answer)
	writeAnswers(ans,fout)
	fin.close()
	fout.flush()
	fout.close()