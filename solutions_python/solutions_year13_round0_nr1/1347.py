f = open('A-large.in', 'r')

N = int(f.readline())

boards = []
results = []

for i in range(N):
	boards.append(f.readline()[:4] + f.readline()[:4] + f.readline()[:4] + f.readline()[:4])
	results.append('Game has not completed')
	f.readline()

def letter_or_T(word, letter):
	if word == letter or word == 'T':
		return True

def win(board, l):
	for i in range(4):
		if letter_or_T(board[4 * i], l) and letter_or_T(board[4 * i + 1], l) and letter_or_T(board[4 * i + 2], l) and letter_or_T(board[4 * i + 3], l):
			return True
		if letter_or_T(board[i], l) and letter_or_T(board[i + 4], l) and letter_or_T(board[i + 8], l) and letter_or_T(board[i + 12], l):
			return True
	if letter_or_T(board[3], l) and letter_or_T(board[6], l) and letter_or_T(board[9], l) and letter_or_T(board[12], l):
		return True
	if letter_or_T(board[0], l) and letter_or_T(board[5], l) and letter_or_T(board[10], l) and letter_or_T(board[15], l):
		return True
	return False

for i in range(N):
	if win(boards[i], 'X'):
		results[i] = 'X won'
	elif win(boards[i], 'O'):
		results[i] = 'O won'
	elif not '.' in boards[i]:
		results[i] = 'Draw'
	print("Case #" + str(i + 1) + ": " + results[i])
