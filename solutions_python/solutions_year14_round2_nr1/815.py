T = input()

def tokenize(inp):
	tokens = []
	curCount = 0
	prevChar = None
	for index,c in enumerate(inp):
		if c != prevChar:
			if prevChar != None:
				tokens.append((prevChar,curCount))
			curCount = 1
		else:
			curCount += 1
		if(index == len(inp)-1):
			tokens.append((c,curCount))
		prevChar = c
	return tokens

fOut = open('repeater.out','w')
for testCase in range(T):
	N = input()
	strings = []
	tokenizedStrings = []
	averages = []

	isPossible = True
	for i in range(N):
		inp = raw_input()
		strings.append(inp)
		tokenizedStrings.append(tokenize(inp))
		if(i>0):
			if(len(tokenizedStrings[i]) != len(tokenizedStrings[i-1])):
				isPossible = False
				break
			
			for index,token in enumerate(tokenizedStrings[i]):
				if(token[0] != tokenizedStrings[i-1][index][0]):
					isPossible = False
					break

		if not isPossible:
			break

		for index,token in enumerate(tokenizedStrings[i]):
			if(i > 0):
				averages[index] += token[1]
			else:
				averages.append(token[1])


	fOut.write('Case #%d: '%(testCase+1))
	if not isPossible:
		fOut.write('Fegla Won')
	else:
		moves = 0
		print averages
		for i in range(N) :
			for index,token in enumerate(tokenizedStrings[i]):
				avg = float(averages[index])/N
				avg = round(avg)
				moves += abs(token[1] - avg)
		fOut.write(str(int(moves)))

	if(testCase != T-1):
		fOut.write('\n')

fOut.close()





