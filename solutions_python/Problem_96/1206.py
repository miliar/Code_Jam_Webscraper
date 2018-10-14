def checkP(score, p):
	for a in range(10, -1, -1):
		
		for b in range(a, a-2, -1):

			if (b < 0):
				continue
			for c in range(b, a-2, -1):
				if (c < 0):
					continue
				#print str(a) + " " + str(b) + " " + str(c)
				if (a+b+c == score and a >= p):
					return True
				elif (a+b+c < score):
					return False
				

def checkSurpriseP(score, p):
		for a in range(10, -1, -1):
			for b in range(a, a-3, -1):
				if (b < 0):
					continue
				for c in range(b, a-3, -1):
					if (c < 0):
						continue
					if (a+b+c == score and a >= p):
						return True
					elif (a+b+c < score):
						return False

def count(surprises, p, scores):
	tot = 0
	for score in scores:
		if (checkP(score, p)):
			tot = tot + 1
		
		elif (surprises > 0 and checkSurpriseP(score, p)):
			surprises = surprises -1
			tot = tot + 1
			
	return tot

counter = 0;
output = open('output.txt', 'w')
with open('input.txt', 'r') as f:
	for fileLine in f:
		if (counter == 0):
			counter = counter + 1
			continue
		fileLine = fileLine.split()
		googlers = int(fileLine[0])
		surprises = int(fileLine[1])
		p = int(fileLine[2])
		scores = []
		for i in range(3, googlers+3):
			scores.append(int(fileLine[i]))
		output.write("Case #" + str(counter) + ": " + str(count(surprises, p, scores)) + "\n")
		counter = counter + 1
		
		
output.close()
f.close()

