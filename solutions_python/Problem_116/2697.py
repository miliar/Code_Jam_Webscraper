import sys

def main():
	file_name = sys.argv[1]
	input_file = open(file_name, 'r')
	output_file = open('output.out', 'w')
	
	T = int(input_file.readline())
	
	for i in range(T):
		if i != 0:
			temp = input_file.readline()
			
		xwon = False
		owon = False
		draw = False
			
		row_board = [input_file.readline().strip('\n') for j in range(4)]
		
		col_board = list()		
		for j in range(4):
			column = ''
			for row in row_board:
				column = column + row[j]
			col_board.append(column)
			
		diagonal1 = ''
		diagonal2 = ''
		for j in range(4):
			diagonal1 += row_board[j][j]
			diagonal2 += row_board[j][3-j]	
		
		for row in row_board:
			if (row.count('X') == 4) or (row.count('X') == 3 and 'T' in row):
				xwon = True
			elif (row.count('O') == 4) or (row.count('O') == 3 and 'T' in row):
				owon = True
		
		if not xwon and not owon:		
			for col in col_board:
				if (col.count('X') == 4) or (col.count('X') == 3 and 'T' in col):
					xwon = True
				elif (col.count('O') == 4) or (col.count('O') == 3 and 'T' in col):
					owon = True
					
			if not xwon and not owon:		
				if (diagonal1.count('X') == 4) or (diagonal1.count('X') == 3 and 'T' in diagonal1):
					xwon = True
				if (diagonal2.count('X') == 4) or (diagonal2.count('X') == 3 and 'T' in diagonal2):
					xwon = True
				if (diagonal1.count('O') == 4) or (diagonal1.count('O') == 3 and 'T' in diagonal1):
					owon = True
				if (diagonal2.count('O') == 4) or (diagonal2.count('O') == 3 and 'T' in diagonal2):
					owon = True
			
		gamecomplete = True
		
		if not xwon and not owon:
			for row in row_board:
				if row.count('X') == 0 or row.count('O') == 0:
					gamecomplete = False
			if not gamecomplete:		
				for col in col_board:
					if col.count('X') == 0 or col.count('O') == 0:
						gamecomplete = False
						
				if diagonal1.count('X') == 0 or diagonal1.count('O') == 0:
					gamecomplete = False
					
				if diagonal2.count('X') == 0 or diagonal2.count('O') == 0:
					gamecomplete = False
				
		if xwon:
			message = 'X won'
		elif owon:
			message = 'O won'
		elif gamecomplete:
			message = 'Draw'
		elif not gamecomplete:
			message = 'Game has not completed'
			
		output_file.write('Case #%d: %s\n' % (i + 1, message))
			
	output_file.close()
	input_file.close()
	

if __name__ == '__main__':
	main()
