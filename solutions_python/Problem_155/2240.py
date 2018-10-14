import pdb

def printCase(x, maxShyness, shyVector):
	peopleStanding = 0
	peopleNeeded = 0
	i = 0
	while (i < len(shyVector)):
		if peopleStanding >= i:
			peopleStanding += int(shyVector[i])
		else:
			delta = i - peopleStanding
			peopleStanding += delta + int(shyVector[i])
			peopleNeeded += delta
		i+=1
	print "Case #" + repr(x) + ": " + repr(peopleNeeded)

T = int(raw_input())

for x in range(1, T+1):
	line = raw_input()
	maxShyness = int(line.split()[0])
	shyVector = line.split()[1]
	printCase(x, maxShyness, shyVector)
