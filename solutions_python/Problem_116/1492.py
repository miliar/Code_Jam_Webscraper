#!/usr/bin/env python

def analyzeGame(game):
	# check horizontal win for X
	for x in range(4):
		if (game[x][0] == 'X' or game[x][0] == 'T') and (game[x][1] == 'X' or game[x][1] == 'T') and (game[x][2] == 'X' or game[x][2] == 'T') and (game[x][3] == 'X' or game[x][3] == 'T'):
			return "X won"
		elif (game[0][x] == 'X' or game[0][x] == 'T') and (game[1][x] == 'X' or game[1][x] == 'T') and (game[2][x] == 'X' or game[2][x] == 'T') and (game[3][x] == 'X' or game[3][x] == 'T'):
			return "X won"
	# check vertical and horizontal win for O
	for y in range(4):
		if (game[y][0] == 'O' or game[y][0] == 'T') and (game[y][1] == 'O' or game[y][1] == 'T') and (game[y][2] == 'O' or game[y][2] == 'T') and (game[y][3] == 'O' or game[y][3] == 'T'):
			return "O won"
		elif (game[0][y] == 'O' or game[0][y] == 'T') and (game[1][y] == 'O' or game[1][y] == 'T') and (game[2][y] == 'O' or game[2][y] == 'T') and (game[3][y] == 'O' or game[3][y] == 'T'):
			return "O won"
	# check forward diagonal win for X
	if (game[0][0] == 'X' or game[0][0] == 'T') and (game[1][1] == 'X' or game[1][1] == 'T') and (game[2][2] == 'X' or game[2][2] == 'T') and (game[3][3] == 'X' or game[3][3] == 'T'):
		return "X won"
	# check forward diagonal win for O
   	if (game[0][0] == 'O' or game[0][0] == 'T') and (game[1][1] == 'O' or game[1][1] == 'T') and (game[2][2] == 'O' or game[2][2] == 'T') and (game[3][3] == 'O' or game[3][3] == 'T'):
   		return "O won"
	# check backward diagonal win for X
   	if (game[0][3] == 'X' or game[0][3] == 'T') and (game[1][2] == 'X' or game[1][2] == 'T') and (game[2][1] == 'X' or game[2][1] == 'T') and (game[3][0] == 'X' or game[3][0] == 'T'):
   		return "X won"
	# check backward diagonal win for O
	if (game[0][3] == 'O' or game[0][3] == 'T') and (game[1][2] == 'O' or game[1][2] == 'T') and (game[2][1] == 'O' or game[2][1] == 'T') and (game[3][0] == 'O' or game[3][0] == 'T'):
		return "O won"
	else:
		for line in game:
			for char in line:
				if char == '.':
					return "Game has not completed"
		return "Draw"

if __name__ == "__main__":

    #input_file="A-small-attempt2.in"
    input_file="A-Large.in"
    fin = open(input_file)
    
    # fout=open('ticTacToe.txt','w')
    fout=open('ticTacToeLarge.txt','w')


    testCases = int(fin.readline().rstrip()) 

    for i in range(1, testCases+1):
    	case = "Case #%d: " %(i)
        fout.write(case)
        game = []
        for y in range(4):
        	game.append(list(fin.readline().rstrip()))
        result = analyzeGame(game)
        fin.readline()
        fout.write(result + "\n")

    fout.close()
    fin.close()