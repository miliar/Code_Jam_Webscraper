from pprint import pprint
import sys

file = open("input2.txt")

nbCases = int(file.readline())
idCase = 0

for line in file.readlines():
	idCase += 1
	line = line.strip()
	tokens = line.split(' ')	
	nbDancers = int(tokens[0])
	nbSurprises = int(tokens[1])
	p = int(tokens[2])
	scores = []
	for i in range(3,len(tokens)):
		scores.append(int(tokens[i]))
	
	
	winners = 0
	for score in scores:
		quotient = score // 3
		remainder = score % 3
		if quotient >= p:
			winners += 1
			continue
		if remainder == 0:
			if quotient > 0 and quotient == (p - 1) and nbSurprises > 0:
				nbSurprises -= 1
				winners += 1
		elif remainder == 1:
			if quotient == (p - 1):
				winners += 1
		elif remainder == 2:
			if quotient == (p - 1):
				winners += 1
			elif quotient == (p - 2) and nbSurprises > 0:
				nbSurprises -= 1
				winners += 1		
	
	print "Case #" + str(idCase) + ": " + str(winners)
