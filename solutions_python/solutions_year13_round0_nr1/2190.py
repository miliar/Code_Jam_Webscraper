def check(row):
	if (row.count('X') == 3 and row.count('T') == 1) or row.count('X') == 4:
		return 'X'
	elif (row.count('O') == 3 and row.count('T') == 1) or row.count('O') == 4:
		return 'O'
	else:
		return -1;


def getboardpositions(board):
	for i in range(4):
		board.append(raw_input())

	raw_input()
	return board


def getcolumns(board):
	cols =  map(list, zip(*board))
	cols = [''.join(i) for i in cols]
	return cols	



def getdiagonals(board):

	diags = []
	new_board = [i[::-1] for i in board]
	left_diag = [board[i][j] for i in range(4) for j in range(4) if i == j]
	right_diag = [new_board[i][j] for i in range(4) for j in range(4) if i == j]
	diags.append(''.join(left_diag))
	diags.append(''.join(right_diag))
	return diags


def checkrows(board,i):
	for r in board:
		if check(r) != -1:
			temp =  "Case #"+ str(i) +": "+str(check(r))+" won"+"\n"
			print temp
			return True
	return False

def main():
	
	n = int(raw_input())
	i = 1

	while i <= n:
		finished = 0
		board = []
		getboardpositions(board)
		diagonals = getdiagonals(board)
		columns = getcolumns(board)
		if (checkrows(board,i)):
			i += 1
			continue;
		
		elif (checkrows(columns,i)):
			i += 1
			continue;
			
		elif (checkrows(diagonals,i)):
			i += 1
			continue;

		else:
			temp = ''.join(board)
			if temp.count('X') + temp.count('O') + temp.count('T') != 16:
				temp =  "Case #"+ str(i) +": "+"Game has not completed\n"
				print temp
			else:
				temp = "Case #"+ str(i) +": "+"Draw"
				print temp


			i += 1

main()
