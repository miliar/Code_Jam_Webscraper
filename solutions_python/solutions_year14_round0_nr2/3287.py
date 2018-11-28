import sys
defaultRate = 2.0

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
	X = data['goal']
	C = data['farmCost']
	F = data['rateAdd']
	R = defaultRate
	bestTime = sys.float_info.max
	newTime = X / R
	farmTime = 0
	while newTime < bestTime:
	  bestTime = newTime
	  farmTime += C / R
	  R += F
	  newTime = farmTime + X / R
	
	return "%.7f" % bestTime
	
if len(sys.argv) > 1:
	fin = file(sys.argv[1])
	fout = file(getOutputName(sys.argv[1]),'w')
	count = 0
	
	numTC = int(fin.readline())
	

	ans = []
	for case in range(numTC):
		data = None
		###### Read in data here from fin, and parse answers.
		[C, F, X] = [float(x) for x in fin.readline().split(' ')]
		data = {"farmCost": C, "rateAdd": F, "goal": X}
		##### put into some type of readable format.
		##### process the data
		answer = doTrial(data)
		print answer
		ans.append(answer)
	writeAnswers(ans,fout)
	fin.close()
	fout.flush()
	fout.close()