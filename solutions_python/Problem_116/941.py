from pprint import pprint

def main():
	with open('A-large.in') as f:
		ntests = int(f.readline())
		arrays = []
		array = []
		i = 1
		for line in f.readlines():
			if line == '\n':
				print "Case #%d: %s" % (i, treat_case(array))
				i += 1
				array = []
			else:
				array.append(list(line)[:-1])

def treat_case(array):
	x_line, o_line = treat_lines(array)
	x_col, o_col =  treat_columns(array)
	x_dia, o_dia = treat_diagonals(array)

	x_won =  x_line or x_col or x_dia
	o_won =  o_line or o_col or o_dia
	
	if x_won:
		result =  "X won"
	elif o_won:
		result = "O won"
	else:
		for line in array:
			if '.' in line:
				result = "Game has not completed"
				break
		else:
			result = "Draw"
	return result


def treat_diagonals(array):
	diagonal_right = []
	diagonal_left = []
	for i in range(4):
		diagonal_right.append(array[i][i])
		diagonal_left.append(array[i][3-i])
	return treat_lines([diagonal_left, diagonal_right])


def treat_columns(array):
	flipped_array = []
	line = []
	for i in range(4):
		line = [line[i] for line in array] 
		flipped_array.append(line)
	return treat_lines(flipped_array)

def treat_lines(array):
	x_won = o_won = False
	for line in array:
		x_count = line.count('X')
		o_count = line.count('O')
		t = 'T' in line
		if x_count == 4 or (x_count == 3 and t):
			x_won = True
		if o_count == 4 or (o_count == 3 and t):
			o_won = True
	return (x_won, o_won)

main()