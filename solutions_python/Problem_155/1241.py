# ================ UTILS START =========================
Case = 0
def readAndExecute(filename, testBlockSize, testFunction):
	with open(filename) as f: 
		T = int(f.readline().strip())
		for t in xrange(T):
			lines = []
			for l in xrange(testBlockSize):
				lines.append(f.readline().strip())
			testFunction(lines)

def formatAnswer(answer):
	global Case
	Case += 1 
	return "Case #"+ str(Case) + ": " + str(answer)

# ================ UTILS END =========================


def opera(line):
	args = line[0].split(" ")
	s_max = args[0]
	s_string = [int(x) for x in args[1]]
	soFar = s_string[0]
	friends = 0
	for shy, count in enumerate(s_string[1:]):
		shy+=1
		diff = max(shy - soFar, 0)
		friends += diff
		soFar += diff + count
	print formatAnswer(friends)
readAndExecute("A-large.in", 1, opera)