def parse(input):
	answer = int(input.readline())
	grid = []
	for i in range(4):
		line = input.readline()
		grid.append(set([int(x) for x in line.split(" ")]))
	return answer, grid

def execute(input):
	numCases = int(input.readline())
	for case in range(1, numCases+1):
		firstAnswer, firstGrid = parse(input)
		secondAnswer, secondGrid = parse(input)
		intersection = firstGrid[firstAnswer-1] & secondGrid[secondAnswer-1]
		if len(intersection) == 1:
			print "Case #{case}: {card}".format(case=case, card=intersection.pop())
		elif len(intersection) > 1:
			print "Case #{case}: Bad magician!".format(case=case)
		elif len(intersection) == 0:
			print "Case #{case}: Volunteer cheated!".format(case=case)


f = open('A-small-attempt0.in')
execute(f)
f.close()