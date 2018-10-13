import copy

def solveD():
	fileIn = open("in.txt", "r")
	lines = [line.strip() for line in fileIn]
	fileIn.close()
	
	fileOut = open("out.txt", "w")
	
	
	T = int(lines[0])
	count = 0
	i = 2
	while count < T:
		a = [float(s) for s in lines[i].split(" ")]
		b = [float(s) for s in lines[i+1].split(" ")]
		i += 3
		count += 1
		result = "Case #%i: %s\n" % (count, solve(a, b))
		print result
		fileOut.write(result)
	
	fileOut.close()
		
def solve(a1, b1):
	a1.sort()
	b1.sort()
	
	a = copy.deepcopy(a1)
	b = copy.deepcopy(b1)
	
	score = 0
	
	while len(a) > 0:
		chosenA = a[-1]
		a.remove(chosenA)
		
		if chosenA > b[-1]:
			chosenB = b[0]
			score += 1
		else:
			for n in b:
				if n > chosenA:
					chosenB = n
					break
		b.remove(chosenB)
	
	a = copy.deepcopy(a1)
	b = copy.deepcopy(b1)
	
	
	betterScore = 0
	
	while len(a) > 0:
		chosenA = a[-1]
		a.remove(chosenA)
		
		if chosenA < b[0]:
			chosenB = b[0]
		else:
			for n in reversed(b):
				if n < chosenA:
					chosenB = n
					betterScore += 1
					break
		b.remove(chosenB)
	
	
	
	return "%i %i" % (betterScore, score)
	
solveD()