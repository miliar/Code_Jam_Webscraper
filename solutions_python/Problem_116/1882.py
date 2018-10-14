winning_rows = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15], # Horizontal
				[0,4,8,12], [1,5,9,13], [2,6,10,14], [3,7,11,15], # Vertical
				[0,5,10,15], [12,9,6,3]]						  # Diagonal

def is_winner(row):
	counts = {'X': 0, 'O': 0, '.': 0, 'T': 0}
	for x in range(0,4):
		counts[row[x]] += 1
		
	if counts['.'] != 0:
		return [False, False]
	elif counts['X'] == 4:
		return ["X won", True]
	elif counts['O'] == 4:
		return ["O won", True]
	elif counts['X'] == 3 and counts['T'] == 1:
		return ["X won", True]
	elif counts['O'] == 3 and counts['T'] == 1:
		return ["O won", True]
	else:
		return [False, True]
	
lines = open("A-large.in", "r").read().splitlines()
num_cases = int(lines[0])

for x in range(0, num_cases):
	board = lines[x*5+1] + lines[x*5+2] + lines[x*5+3] + lines[x*5+4]
	is_full = True
	
	for row in winning_rows:
		[winner, is_row_full] = is_winner([board[row[0]], board[row[1]], board[row[2]], board[row[3]]])
		
		if winner:
			print "Case #%d: %s" % (x+1, winner)
			break
		else:
			if not is_row_full:
				is_full = False
	else:
		if is_full:
			print "Case #%d: Draw" % (x+1)
		else:
			print "Case #%d: Game has not completed" % (x+1)