# Javier Fernandez Google Code Jam 2013
# Google Code Jam 2013
# javierfdr@gmail.com - javierfdr
# Tic Tac Toe Tomek

import sys

# return 10 poosible character strikes
def process_board(ia):
	strikes = [[],[],[],[],[],[],[],[],[],[]]
	strikes[0] = ia[0]
	strikes[1] = ia[1]
	strikes[2] = ia[2]
	strikes[3] = ia[3]
	strikes[4] = [ia[0][0],ia[1][0],ia[2][0],ia[3][0]]
	strikes[5] = [ia[0][1],ia[1][1],ia[2][1],ia[3][1]]
	strikes[6] = [ia[0][2],ia[1][2],ia[2][2],ia[3][2]]
	strikes[7] = [ia[0][3],ia[1][3],ia[2][3],ia[3][3]]
	strikes[8] = [ia[0][0],ia[1][1],ia[2][2],ia[3][3]]
	strikes[9] = [ia[3][0],ia[2][1],ia[1][2],ia[0][3]]

	return strikes

# create 10 possible winning strikes from 4 input array
def numerize_board(ia):
	num_strikes = []
	for row in ia:
		num_strikes.append(numerize_input(row))

	return num_strikes

# transform from characters to input. X-1, O-1, T-0
def numerize_input(a):
	b = []
	for i in a:
		if i=='T':
			b.append(0)
		elif i=='O':
			b.append(1)
		elif i=='X':
			b.append(-1)
	return b

# if row is filled with X or O or there is a T then is winning
def is_winning_row(char_row, num_row):
	s = sum(num_row)
	if s==3 or s==-3:
		if 'T' in char_row:
			return s
	if s==4 or s==-4:
		return s
	
	if len(num_row)==4:
		return 10 # for filled row
	else:
		return 0 #for non-finished

def solve_tic_tac(ia):
	char_strikes = process_board(ia)
	num_strikes = numerize_board(char_strikes)

	full_rows = 0

	for r in range(10):

		w = is_winning_row(char_strikes[r],num_strikes[r])
		if w==3 or w==4:
			return 'O won'
		elif w==-3 or w==-4:
			return 'X won'
		elif w==10:
			full_rows = full_rows+1

	if full_rows == 10:
		return 'Draw'
	else:
		return 'Game has not completed'
		


out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline())
for c in range(1,num_cases+1):
	case = 'Case #'+str(c)+': '
	r = []
	r.append(list(in_file.readline().strip('\n')))
	r.append(list(in_file.readline().strip('\n')))
	r.append(list(in_file.readline().strip('\n')))
	r.append(list(in_file.readline().strip('\n')))
	in_file.readline().strip('\n').split()

	s = solve_tic_tac(r)

	result = case+s+'\n'
	out_file.write(result)



