import random

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
winners = [
2*3*5*7, 11*13*17*19, 23*29*31*37, 41*43*47*53, # horizontal
2*11*23*41, 3*13*29*43, 5*17*31*47, 7*19*37*53, # vertical
2*13*31*53, 7*17*29*41							# diagonal
]
winners = map(float, winners)

output = open('output.txt', 'w')


def solve(board):
	board = board.replace('\n', '')

	Xmul = 1
	Omul = 1

	for prime, character in zip(primes, board):
		if character == 'X':
			Xmul *= prime
		elif character == 'O':
			Omul *= prime
		elif character == 'T':
			Xmul *= prime
			Omul *= prime

	X = any([Xmul % winner == 0 for winner in winners])
	O = any([Omul % winner == 0 for winner in winners])

	if X:
		return 'X won'
	elif O:
		return 'O won'
	else:	# No one has won yet
		if '.' in board:
			return 'Game has not completed'
		else:
			return 'Draw'

input = open('input.txt', 'r')
numGrids = int(input.readline())
gridNumber = 0
print numGrids
for i in range(1, numGrids+1):
	board = []
	for line in range(4):
		board.append(input.readline())
	result = solve(''.join(board))
	output.write('Case #%s: %s\n' % (i, result))
	# skip ahead
	input.readline()

input.close()
output.close()
