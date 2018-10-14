from pprint import pprint as pp
ncases = int(raw_input().strip())
# for case_i in range(nc):

# Lambda methods
is_not_x = lambda move: move!='X' and move!='.'
is_not_o = lambda move: move!='O' and move!='.'
is_win_for_x = lambda row: len(filter( is_not_o, row )) == 4
is_win_for_o = lambda row: len(filter( is_not_x, row )) == 4

def output_result( case, result ):
	results = {
		'x' : 'X won',
		'o' : 'O won',
		'd' : 'Draw',
		'n' : 'Game has not completed'
	}
	print "Case #%d: %s" % (case+1,results[result])

# Case #1: 
# Case #2: Draw
# Case #3: Game has not completed
# Case #4: O won
# Case #5: O won
# Case #6: O won

for case_i in range(ncases):

	is_win_o = False
	is_win_x = False
	is_draw = False
	is_none = False
	can_draw = True

	matrix = []
	matrix_t = [ [] ] * 4
	d1 = []
	d2 = []

	# try:

	for line_i in range(4):
		line = raw_input().strip()

		if can_draw and '.' in line:
			can_draw = False

		row = list(line.strip())
		matrix.append( row )

	matrix_t = zip(*matrix)
	d1 = [ matrix[i][i] for i in range(4) ]
	d2 = [ matrix_t[3-i][i] for i in range(4) ]

	# print d1
	# print d2

	# pp(matrix)
	# break

	for i in range(4):
		row = matrix[i]
		col = matrix_t[i]

		is_win_o = is_win_o or len(filter( is_not_x, row )) == 4
		is_win_o = is_win_o or len(filter( is_not_x, col )) == 4

		if is_win_o or is_win_x:
			break

		is_win_x = is_win_x or len(filter( is_not_o, row )) == 4
		is_win_x = is_win_x or len(filter( is_not_o, col )) == 4

		if is_win_o or is_win_x:
			break

	if not is_win_x and not is_win_o:
		is_win_o = is_win_o or len(filter( is_not_x, d1 )) == 4
		is_win_o = is_win_o or len(filter( is_not_x, d2 )) == 4

	if not is_win_x and not is_win_o:
		# print 'checking diags'
		is_win_x = is_win_x or len(filter( is_not_o, d1 )) == 4
		is_win_x = is_win_x or len(filter( is_not_o, d2 )) == 4

	if is_win_x:
		output_result(case_i,'x')
	elif is_win_o:
		output_result(case_i,'o')
	elif not is_win_x and not is_win_o and can_draw:
		output_result(case_i,'d')
	elif not is_win_x and not is_win_o and not can_draw:
		output_result(case_i,'n')

	# print is_win_x, is_win_o

	# print '='*40

	try:
		raw_input()
	except:
		break