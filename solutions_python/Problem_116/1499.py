import sys
import shlex

f = open('small.in', 'r')
g = open('small.out', 'w')

T = int(f.readline())
board = []
test_num = 0

def main():
	global test_num, board
	
	for sets in range(T):
		test_num = sets
		board = []
		board.append(str.strip(f.readline()))		# row 1
		board.append(str.strip(f.readline()))		# row 2
		board.append(str.strip(f.readline()))		# row 3
		board.append(str.strip(f.readline()))		# row 4
		
		horizontal_win = False
		vertical_win = False
		diagonal_win = False
		win_draw = False
		
		# Horizontal Test
		win_draw = horizontal_test()
		
		# Verticle Test
		if win_draw == False:
			win_draw = verticle_test()
		
		# Diagonal Test
		if win_draw == False:
			win_draw = diagonal_test()
			
		# Draw / In Progress Test
		if win_draw == False:
			win_draw = draw_test()
					
		f.readline()		# blank line		
		
	f.close()
	g.close()
	sys.exit()


def horizontal_test():
	for row in board:
		o_line = False
		x_line = False
		o_lose = False
		x_lose = False
		
		for column in row:
			if column == '.':
				o_lose = True
				x_lose = True
				break
			if (o_line == False) and (x_line == False) and (column == 'O'):
				o_line = True
				x_lose = True
			if (x_line == False) and (o_line == False) and (column == 'X'):
				x_line = True
				o_lose = True
				
			if (o_line == True) and (column == 'X'):
				o_lose = True
				break
			elif (x_line == True) and (column == 'O'):
				x_lose = True
				break
		
		if x_lose == False and o_lose == False:
			print("Error: ", board)
			return False
		elif x_lose == False:
			print_x_win()
			return True
		elif o_lose == False:
			print_o_win()
			return True
			
	return False
	

def verticle_test():
	for column in range(len(board[0])):
		o_line = False
		x_line = False
		o_lose = False
		x_lose = False
		
		for row in board:
			if row[column] == '.':
				o_lose = True
				x_lose = True
				break
			if (o_line == False) and (x_line == False) and (row[column] == 'O'):
				o_line = True
				x_lose = True
			if (x_line == False) and (o_line == False) and (row[column] == 'X'):
				x_line = True
				o_lose = True
				
			if (o_line == True) and (row[column] == 'X'):
				o_lose = True
				break
			elif (x_line == True) and (row[column] == 'O'):
				x_lose = True
				break
		
		if x_lose == False and o_lose == False:
			print("Error: ", board)
			return False
		elif x_lose == False:
			print_x_win()
			return True
		elif o_lose == False:
			print_o_win()
			return True
	
	return False
		
		
def diagonal_test():
	o_line = False
	x_line = False
	o_lose = False
	x_lose = False
	
	o_line_rev = False
	x_line_rev = False
	o_lose_rev = False
	x_lose_rev = False
	
	for row in range(len(board)):
		column = row
		reverse =  (-1 * column) - 1
		
		if board[row][column] == '.':
			o_lose = True
			x_lose = True
		if board[row][reverse] == '.':
			o_lose_rev = True
			x_lose_rev = True
		
		if (o_line == False) and (x_line == False) and (board[row][column] == 'O'):
			o_line = True
			x_lose = True
		if (x_line == False) and (o_line == False) and (board[row][column] == 'X'):
			x_line = True
			o_lose = True
		
		if (o_line_rev == False) and (x_line_rev == False) and (board[row][reverse] == 'O'):
			o_line_rev = True
			x_lose_rev = True
		if (x_line_rev == False) and (o_line_rev == False) and (board[row][reverse] == 'X'):
			x_line_rev = True
			o_lose_rev = True
			
		if (o_line == True) and (board[row][column] == 'X'):
			o_lose = True
		elif (x_line == True) and (board[row][column] == 'O'):
			x_lose = True
		
		if (o_line_rev == True) and (board[row][reverse] == 'X'):
			o_lose_rev = True
		elif (x_line_rev == True) and (board[row][reverse] == 'O'):
			x_lose_rev = True
	
	if ((x_lose == False and o_lose == False) or
		(x_lose_rev == False and o_lose == False) or
		(x_lose == False and o_lose_rev == False) or
		(x_lose_rev == False and o_lose_rev == False)):
		print("Error: ", board)
		return False
	elif x_lose == False:
		print_x_win()
		return True
	elif o_lose == False:
		print_o_win()
		return True
	elif x_lose_rev == False:
		print_x_win()
		return True
	elif o_lose_rev == False:
		print_o_win()
		return True
	else:
		return False
		
		
def draw_test():
	for row in board:
		for column in row:
			if (column == '.'):
				print_in_progress()
				return False
			
	print_draw()
	return True


def print_x_win():
	g.write("Case #" + str(test_num+1) + ": X won\n")
	return
				
def print_o_win():
	g.write("Case #" + str(test_num+1) + ": O won\n")
	return
	
def print_draw():
	g.write("Case #" + str(test_num+1) + ": Draw\n")
	return
	
def print_in_progress():
	g.write("Case #" + str(test_num+1) + ": Game has not completed\n")
	return
	
	
main()