
def problemB(inputFile,outputFile):
	f = open(inputFile,"r")
	input = f.readlines()
	output = ""

	for i, line in enumerate(input[1:]):
		output += "Case #" + str(i+1) + ": " + str(parseLine(line)) + "\n"
	
	g = open(outputFile,"w")
	g.write(output)
	g.close()
	f.close()

def parseLine(line):
	numbers = line.split()
	S = int(numbers[1])
	p = int(numbers[2])
	
	count = 0
	for score in numbers[3:]:
		score = int(score)
		v = highScore(score,p)
		if v == 1:
			count += 1
		elif v == 0:
			if S > 0:
				count += 1
				S -= 1
	return count

"""
	Return 1 if p can be obtained naturally
	Return 0 if p can be obtained with the use of a surprising judgement
	Return -1 if p cannot be obtained
"""
def highScore(score,p):
	if p != 0 and score == 0:
		return -1
	elif p == 10 and score < 30:
		return -1
	elif 3*p <= score+2:
		return 1
	elif 3*p <= score+4:
		return 0
	else:
		return -1


problemB("p2-input.txt","p2-output.txt")
