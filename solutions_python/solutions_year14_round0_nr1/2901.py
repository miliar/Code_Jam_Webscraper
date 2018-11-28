import sys

T = int(sys.stdin.readline())

for i in range(T):

	pos = int(sys.stdin.readline())

	board = []

	for j in range(4):
		board.append(sys.stdin.readline().rstrip().split(' '))

	candidates = set(board[pos-1])
	#print candidates

	pos = int(sys.stdin.readline())

	board = []

	for j in range(4):
		board.append(sys.stdin.readline().rstrip().split(' '))

	#print set(board[pos-1])

	candidates &= set(board[pos-1])

	print "Case #"+str(i+1)+':',

	if len(candidates) == 1:
		for card in candidates:
			print card
	elif len(candidates) == 0:
		print "Volunteer cheated!"
	else:
		print "Bad magician!"
