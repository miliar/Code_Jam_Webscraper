#!/usr/bin/python3

def readInputFile():
	l = [line.rstrip('\n') for line in open('in.in')]
	return l

def putOutpinutFile(testCaseResults):
	f = open('out.out', 'w')
	i = 1
	for row in testCaseResults:
 		f.write('Case #' + str(i) + ': ' + row + '\n')
 		i += 1



def calcWinner(g):
	'''[X, R, C] := X-omino, RxC field '''
	x = int(g[0])
	r = int(g[1])
	c = int(g[2])
	fieldSize = r*c

	# FieldSize is not a multiple of X-omino → Richard
	if fieldSize % x != 0:
		return 'RICHARD'

	if fieldSize < x:
		return 'RICHARD'

	# If the field is a x*1 or 1*x, richard can chose a x so Garbial cant win
	if min(r, c) < 2 and x > 2:
		return 'RICHARD'

	
	''' fieldsize 8 or 2x2 field, with this one:
	 x
	xxx 
	or
	xx
	xx
	then Richard wins
	'''
	if (fieldSize == 8 or (r == 2 and c == 2)) and x == 4:
		return 'RICHARD'


	# cases did not catch game
	return 'GABRIEL'


lines = readInputFile()[1::]
games = list(map(lambda x: x.split(), lines))

putOutpinutFile([calcWinner(g) for g in games])