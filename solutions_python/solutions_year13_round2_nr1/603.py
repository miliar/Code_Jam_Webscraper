import fileinput

def eat(motes, arminSize):
	eatenMotes = 0
	for mote in motes:
		if mote < arminSize:
			arminSize += mote
			eatenMotes += 1
		else:
			break
	# print 'New size', arminSize, 'Ate', eatenMotes
	motes = motes[eatenMotes:]
	return (motes, arminSize)



def eatBig(motes, arminSize, stepsTaken):
	# print 'Steps taken', stepsTaken
	if len(motes) == 0:
		return stepsTaken

	if len(motes) < 2:
		return stepsTaken + 1

	arminGrow = arminSize - 1		
	if arminGrow <= 0:
		return len(motes)

	#Two options:
	firstMotes = motes[:]
	firstMotes.pop()
	firstResult = eatBig(firstMotes, arminSize, stepsTaken + 1)

	secondMotes = motes[:]
	secondArminSize = arminSize + arminGrow
	(secondMotes, secondArminSize) = eat(secondMotes, secondArminSize)
	secondResult = eatBig(secondMotes, secondArminSize, stepsTaken + 1)
	return min(firstResult, secondResult)

	
	# if lastPiece > (arminSize + arminGrow):
	# 	motes.pop()
	# else:
	# 	arminSize += arminGrow
	# 	(motes, arminSize) = eat(motes, arminSize)	
	# return eatBig(motes, arminSize, stepsTaken + 1)

def solve(motes, arminSize):
	motes = sorted(motes)
	(motes, arminSize) = eat(motes, arminSize)
	return eatBig(motes, arminSize, 0)
	


answers = []
inputlines = []
for line in fileinput.input():
	inputlines.append(line)

numberOfCases = int(inputlines[0])
for i in range(numberOfCases):	
	info = inputlines[i*2 + 1].split()
	motes = map(int, inputlines[i*2 + 2].split())
	(arminSize, numberOfMotes) = (int(info[0]), int(info[1]))
	result = solve(motes, arminSize)
	print result
	answer = 'Case #' + str(i + 1) + ': ' + str(result) + '\n'
	answers.append(answer)

with open ('myfile', 'a') as f:
	for answer in answers:
		f.write (answer)