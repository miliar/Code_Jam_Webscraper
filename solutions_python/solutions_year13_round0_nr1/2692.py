#!/usr/bin/python




WINNING_COMBINATIONS = (
	# Horizontal wins
	(0,1,2,3),
	(4,5,6,7),
	(8,9,10,11),
	(12,13,14,15),
	
	# Vertical wins
	(0,4,8,12),
	(1,5,9,13),
	(2,6,10,14),
	(3,7,11,15),

	# Diagnoal 1 win
	(0,5,10,15),
	
	# Diagonal 2 win
	(3,6,9,12)
)

WILDCARD = 'T'

CURRENT_GAME_COMPLETED = False

def check_win(board):
	global CURRENT_GAME_COMPLETED
	CURRENT_GAME_COMPLETED = True
	for win in WINNING_COMBINATIONS:
		p = None
		player_won = 0
		for w in win:
			if board[w] == '.':
				CURRENT_GAME_COMPLETED = False
				break
			if p is None:
				p = board[w]
				player_won += 1
			else:
				if board[w] in (p, WILDCARD):
					player_won += 1

		if player_won == 4:
			return p

write_to_file = ''
filename = 'tttt_real_data.txt'
with open(filename) as f:
	line = f.readline()
	test_cases = int(line.strip('\n'))

	for test_case in range(test_cases):
		current_board = ''

		for x in range(4):
			for x in f.readline():
				current_board += x.strip('\n')

		#print current_board
		f.readline()
		
		winner = check_win(current_board)
		if winner:
			write_to_file += 'Case #%d: %s won\n' % (test_case+1, winner)
		elif CURRENT_GAME_COMPLETED:
			write_to_file += 'Case #%d: Draw\n' % (test_case+1,)
		else:
			write_to_file += 'Case #%d: Game has not completed\n' % (test_case+1,)			

with open('tttt_results.txt', 'w+') as f:
	f.write(write_to_file)
	
