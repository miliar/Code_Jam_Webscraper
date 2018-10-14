# Input data
infile = input("Enter input filename: ") + ".in"
if infile == ".in": infile = "default.in"
with open(infile, 'r') as f:
	data = f.read().split("\n")
while data[-1].isspace() or not(data[-1]):
	data.pop()
	
testCases = int(data[0]) #number of cases
dataL = data.__len__() #length of data

# Functions
def factorString (text):
	"""Factorize string
	e.g. aabbb
	return [[a, b],[2,3]]"""
	base = [text[0]]
	factor = [0]
	for l in text:
		if l == base[-1]:
			factor[-1] += 1
		else:
			base.append(l)
			factor.append(1)
	return [base, factor]

def getMov (M, r, c):
	mov = 0
	for col in range (c):
		avg = 0 #average
		for row in range(r):
			avg += M[row][col]
		avg = round(avg/r)
		for row in range(r):
			mov += abs(M[row][col]-avg)
	return mov

# Problem solution
stringLose = "Fegla Won"
results = []
case = 1
while case < dataL:
	nStringGame = int(data[case]) #number of string in game
							#must be bigger than 1!
	gameString = data[case + 1: case + nStringGame + 1]
	baseString = []
	factors = []
	for word in gameString:
		result = factorString(word) #[Base, Factor]
		if not baseString:
			baseString = result[0]
			factors.append(result[1])
		elif baseString != result[0]: #you Lose
			results.append(stringLose)
		else:	
			factors.append(result[1])
	if factors.__len__() == nStringGame:
		results.append(getMov(factors, nStringGame, baseString.__len__()))
	case += nStringGame +1 #next game
# Output data
outfile = "out.txt"
with open(outfile, 'w') as f:
	for i in range(testCases):
		f.write("Case #%i: %s\n" % (i+1, str(results[i])))
			
