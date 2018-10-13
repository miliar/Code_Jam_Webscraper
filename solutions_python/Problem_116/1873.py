from itertools import groupby
from operator import itemgetter

def decide_status(input_string, case_num):
	# create an array of indices with squares 'friendly' to player X and player O, as well as empty squares
	x_friendly_squares = []
	o_friendly_squares = []
	empty_squares = []
	for i in xrange(0, len(input_string)):
		if input_string[i].lower() == 't':
			x_friendly_squares.append(i)
			o_friendly_squares.append(i)
		elif input_string[i].lower() == 'x':
			x_friendly_squares.append(i)
		elif input_string[i].lower() == 'o':
			o_friendly_squares.append(i)
		elif input_string[i] == '.':
			empty_squares.append(i)
	# detecting consecutive integers in the list [aka x has 4 in a row or o has 4 in a row]
	x_friendly_squares, o_friendly_squares = set(x_friendly_squares), set(o_friendly_squares)
	row1, row2, row3, row4 = set([0,1,2,3]), set([4,5,6,7]), set([8,9,10,11]), set([12,13,14,15])
	if row1.issubset(x_friendly_squares) or row2.issubset(x_friendly_squares) or row3.issubset(x_friendly_squares) or row4.issubset(x_friendly_squares):
		return 'Case #%d: X won\n' % case_num
	elif row1.issubset(o_friendly_squares) or row2.issubset(o_friendly_squares) or row3.issubset(o_friendly_squares) or row4.issubset(o_friendly_squares):
		return 'Case #%d: O won\n' % case_num
	# detecting integers with the same modulo 4 [aka x has 4 in a column or o has 4 in a column]
	# convert to set for easy subset detection
	
	column1, column2, column3, column4 = set([0,4,8,12]), set([1,5,9,13]), set([2,6,10,14]), set([3,7,11,15])
	if column1.issubset(x_friendly_squares) or column2.issubset(x_friendly_squares) or column3.issubset(x_friendly_squares) or column4.issubset(x_friendly_squares):
		return 'Case #%d: X won\n' % case_num
	elif column1.issubset(o_friendly_squares) or column2.issubset(o_friendly_squares) or column3.issubset(o_friendly_squares) or column4.issubset(o_friendly_squares):
		return 'Case #%d: O won\n' % case_num
	# detecting diagonal win
	diagonal1, diagonal2 = set([0,5,10,15]), set([3,6,9,12])
	if diagonal1.issubset(x_friendly_squares) or diagonal2.issubset(x_friendly_squares):
		return 'Case #%d: X won\n' % case_num
	elif diagonal1.issubset(o_friendly_squares) or diagonal2.issubset(o_friendly_squares):
		return 'Case #%d: O won\n' % case_num
		# find out if empty_squares list is empty
	if len(empty_squares) == 0:
		return 'Case #%d: Draw\n' % case_num # game was draw
	return 'Case #%d: Game has not completed\n' % case_num


f = open('A-large.in', 'r')
file_contents = f.readlines()[1:] # excluding the first line which we don't need
f.close()
f = open('A-large.out', 'a')
for line in file_contents:
	if line == '\n':
		file_contents.remove(line)
for i in xrange(4, len(file_contents)+1, 4):
	joined_string = ''.join(file_contents[i-4:i]).replace('\n','')
	f.write(decide_status(joined_string, i/4))
f.close()
