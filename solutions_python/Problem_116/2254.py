import sys

def check_board(board):
	
	for row in board:
		srow = set(row)
		if srow == set(["X", "T"]) or srow == set(["O", "T"]):
			return list(srow - set("T"))[0]
		if srow == set(["X"]) or srow == set(["O"]):
			return list(srow)[0]
	
	for col in range(4):
		srow = set([row[col] for row in board])
		if srow == set(["X", "T"]) or srow == set(["O", "T"]):
		   return list(srow - set("T"))[0]
		if srow == set(["X"]) or srow == set(["O"]):
			return list(srow)[0]
			
	srow = set([board[i][i] for i in range(4)])
	if srow == set(["X", "T"]) or srow == set(["O", "T"]):
	   return list(srow - set("T"))[0]
	if srow == set(["X"]) or srow == set(["O"]):
		return list(srow)[0]

	srow = set([board[i][3 - i] for i in range(4)])
	if srow == set(["X", "T"]) or srow == set(["O", "T"]):
	   return list(srow - set("T"))[0]
	if srow == set(["X"]) or srow == set(["O"]):
		return list(srow)[0]

	for row in board:
		if '.' in row:
			return "Game has not completed"
			
	return "Draw"		
	
		

fil = [i.strip() for i in open('tttt.txt').readlines()]
cases = int(fil[0])

for case in range(1, cases + 1):
	board = fil[1+(case-1)*5:(case*5)]
	result = check_board(board)
	if len(result) == 1:
		result += " won"
	print "Case #{}: {}".format(case, result)