import sys
player1 = 'X'
player2 = 'O'
win = False

def checkwin(player, board):
	for c in range(4):
		if ((board[c][0] == player) or (board[c][0] == 'T')) and ((board[c][1] == player) or (board[c][1] == 'T')) and ((board[c][2] == player) or (board[c][2] == 'T')) and ((board[c][3] == player) or (board[c][3] == 'T')):
			win = True
			return win
		elif ((board[0][c] == player) or (board[0][c] == 'T')) and ((board[1][c] == player) or (board[1][c] == 'T')) and ((board[2][c] == player) or (board[2][c] == 'T')) and ((board[3][c] == player) or (board[3][c] == 'T')):
			win = True
			return win
		elif ((board[0][0] == player) or (board[0][0] == 'T')) and ((board[1][1] == player) or (board[1][1] == 'T')) and ((board[2][2] == player) or (board[2][2] == 'T')) and ((board[3][3] == player) or (board[3][3] == 'T')):
			win = True
			return win
		elif ((board[0][3] == player) or (board[0][3] == 'T')) and ((board[1][2] == player) or (board[1][2] == 'T')) and ((board[2][1] == player) or (board[2][1] == 'T')) and ((board[3][0] == player) or (board[3][0] == 'T')):
			win = True
			return win
	else:
		win = False
		return win

def checkdraw(board):
	counter = 0
	for c in range(4):
		for r in range(4):
			if board[c][r] == 'O':
				counter += 1
			elif board[c][r] == 'X':
				counter += 1
			elif board[c][r] == 'T':
				counter += 1
			else:
				continue
	return counter == 16

def main(file):
	f = open(file, 'r')
	stages = int(f.readline())
	stage = 0
	board = [['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]
	fo = open('A-large.out', 'wd')

	while stage < stages: 
		for da in range(0,4):
			line = f.readline()
			try:
				board[da] = [line[0],line[1],line[2],line[3]]
			except:
				break
		stage += 1
		try:
			f.readline()
		except:
			break
		msg = ""
		if checkwin(player1,board):
			msg = "X won\n"
		elif checkwin(player2,board):
			msg = "O won\n"
		elif checkdraw(board):
			msg = "Draw\n"
		else:
			msg = "Game has not completed\n"
		fo.write("Case #" + str(stage) + ": " + msg)

if __name__ == '__main__':
	main('A-large.in')
