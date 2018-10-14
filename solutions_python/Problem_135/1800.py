import sys

f = open(sys.argv[1])
T = int(f.readline())

def readMatrix():
	return [list(map(int, f.readline().strip().split(' '))) for r in range(4)]

for t in range(T):
	firstAnswer = int(f.readline())
	firstBoard = readMatrix()
	secondAnswer = int(f.readline())
	secondBoard = readMatrix()
	
	firstRow = firstBoard[firstAnswer - 1]
	secondRow = secondBoard[secondAnswer - 1]

	intersection = list(set(firstRow) & set(secondRow))
	if len(intersection) == 0:
		answer = 'Volunteer cheated!'
	elif len(intersection) == 1:
		answer = intersection[0]
	else:
		answer = 'Bad magician!'
	
	print 'Case #%d:' % (t + 1), answer
