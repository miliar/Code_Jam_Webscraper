# Codejam Problem A: Tic-Tac-Toe-Tomek

import re

cj_input = open("a.txt")
cj_output = open("a_out.txt", 'w')
num_games = int(cj_input.readline()) # Get The Number Of Games

# Load Up The Games Into Lists

games = []
for game_num in range(num_games):
	current_game = [];
	for row_num in range(4):
		current_game.append(cj_input.readline().strip())
	cj_input.readline()
	games.append(current_game)

win_X = re.compile("^[XT]{4}$")
win_O = re.compile("^[OT]{4}$")

for game_num, game in enumerate(games):
	case_result = None
	case_num = game_num + 1

	rows = ['','','','']
	collumns = ['','','','']
	diagonals = ['','']

	for line_num, line in enumerate(game):
		rows[line_num] = line # Add To Rows
		# Add To Collumns
		for i in range(4):
			collumns[i] += line[i]
	# Add Diagonals
	diagonals[0] = "{}{}{}{}".format(game[0][0], game[1][1], game[2][2], game[3][3])
	diagonals[1] = "{}{}{}{}".format(game[0][3], game[1][2], game[2][1], game[3][0])

	for row in rows:
		if win_X.match(row):
			case_result = "X won"
			break
		elif win_O.match(row):
			case_result = "O won"
			break
	for collumn in collumns:
		if win_X.match(collumn):
			case_result = "X won"
			break
		elif win_O.match(collumn):
			case_result = "O won"
			break
	for diagonal in diagonals:
		if win_X.match(diagonal):
			case_result = "X won"
			break
		elif win_O.match(diagonal):
			case_result = "O won"
			break

	if case_result == None:
		for line in game:
			if '.' in line:
				case_result = "Game has not completed"
				break
	if case_result == None:
		case_result = "Draw"

	
	case_string = "Case #{}: {}\n".format(case_num, case_result)
	cj_output.write(case_string)

cj_output.close()