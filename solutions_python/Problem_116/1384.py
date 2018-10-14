'''
Code Jam 2013
Tic-Tac-Toe-Tomek
@Jace Maxfield
'''

import sys

def analyzegame():

	#determine horizontal and vertical win for 'X'
	for x in range(4):
		if (gameboard[x][0] == 'X' or gameboard[x][0] == 'T') and (gameboard[x][1] == 'X' or gameboard[x][1] == 'T') and (gameboard[x][2] == 'X' or gameboard[x][2] == 'T') and (gameboard[x][3] == 'X' or gameboard[x][3] == 'T'):
			return 'X won'
		elif (gameboard[0][x] == 'X' or gameboard[0][x] == 'T') and (gameboard[1][x] == 'X' or gameboard[1][x] == 'T') and (gameboard[2][x] == 'X' or gameboard[2][x] == 'T') and (gameboard[3][x] == 'X' or gameboard[3][x] == 'T'):
			return 'X won'
	#determine horizontal and vertical win for 'O'
	for y in range(4):
		if (gameboard[y][0] == 'O' or gameboard[y][0] == 'T') and (gameboard[y][1] == 'O' or gameboard[y][1] == 'T') and (gameboard[y][2] == 'O' or gameboard[y][2] == 'T') and (gameboard[y][3] == 'O' or gameboard[y][3] == 'T'):
			return 'O won'
		elif (gameboard[0][y] == 'O' or gameboard[0][y] == 'T') and (gameboard[1][y] == 'O' or gameboard[1][y] == 'T') and (gameboard[2][y] == 'O' or gameboard[2][y] == 'T') and (gameboard[3][y] == 'O' or gameboard[3][y] == 'T'):
			return 'O won'
	#determine forward diagonal win for 'X'
	if (gameboard[0][0] == 'X' or gameboard[0][0] == 'T') and (gameboard[1][1] == 'X' or gameboard[1][1] == 'T') and (gameboard[2][2] == 'X' or gameboard[2][2] == 'T') and (gameboard[3][3] == 'X' or gameboard[3][3] == 'T'):
		return 'X won'
	#determine forward diagonal win'O'
	elif (gameboard[0][0] == 'O' or gameboard[0][0] == 'T') and (gameboard[1][1] == 'O' or gameboard[1][1] == 'T') and (gameboard[2][2] == 'O' or gameboard[2][2] == 'T') and (gameboard[3][3] == 'O' or gameboard[3][3] == 'T'):
		return 'O won'
	#determine backward diagonal win 'X'
	elif (gameboard[0][3] == 'X' or gameboard[0][3] == 'T') and (gameboard[1][2] == 'X' or gameboard[1][2] == 'T') and (gameboard[2][1] == 'X' or gameboard[2][1] == 'T') and (gameboard[3][0] == 'X' or gameboard[3][0] == 'T'):
		return 'X won'
	#determine backward diagonal win 'O'
	elif (gameboard[0][3] == 'O' or gameboard[0][3] == 'T') and (gameboard[1][2] == 'O' or gameboard[1][2] == 'T') and (gameboard[2][1] == 'O' or gameboard[2][1] == 'T') and (gameboard[3][0] == 'O' or gameboard[3][0] == 'T'):
		return 'O won'
	#no winner
	else:
		for line in gameboard:
			for char in line:
				if char == '.':
					return 'Game has not completed'
		return 'Draw'

if __name__ == '__main__':
	file = open('A-large.in', 'r')
	result = open('large-result.txt', 'w')
	testcases = int(file.readline().rstrip())
	for x in range(testcases):
		gameboard = []
		for y in range(4):
			gameboard.append(list(file.readline().rstrip()))
		result.write('Case #' + str(x+1) + ': ' + analyzegame() + '\n')
		file.readline()
	result.close()