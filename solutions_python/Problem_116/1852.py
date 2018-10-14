
data = open("1.dat").readlines()

import string

data = map(string.strip,data)

num_test_cases = int(data[0])
data = data[1:]

def check_board(b):
	for data_line in b:
		for c in data_line:
			if c == ".":
				pass
			elif c == "T":
				pass
			elif c == "X":
				pass
			elif c == "O":
				pass
			else:
				return False
	return True

def check4(b,sym):
	sym_count = 0
	t_count  = 0
	for c in b:
		if c == sym:
			sym_count = sym_count + 1
		if c == "T":
			t_count = t_count + 1
	if sym_count == 4:
		return True
	if sym_count == 3 and t_count == 1:
		return True
	return False

def check_sym_win(b,sym):
	# horizontal
	if check4(b[0],sym):
		return True
	if check4(b[1], sym):
		return True
	if check4(b[2], sym):
		return True
	if check4(b[3], sym):
		return True
	# vertical
	ts = b[0][0] + b[1][0] + b[2][0] + b[3][0]
	if check4(ts,sym):
		return True
	ts = b[0][1] + b[1][1] + b[2][1] + b[3][1]
	if check4(ts,sym):
		return True
	
	ts = b[0][2] + b[1][2] + b[2][2] + b[3][2]
	if check4(ts,sym):
		return True
	
	ts = b[0][3] + b[1][3] + b[2][3] + b[3][3]
	if check4(ts,sym):
		return True

	# diag 1
	ts = b[0][0] + b[1][1] + b[2][2] + b[3][3]
	if check4(ts,sym):
		return True
	# diag 2
	ts = b[0][3] + b[1][2] + b[2][1] + b[3][0]
	if  check4(ts, sym):
		return True

	return False	

def check_incomplete(b):
	for d in b:
		for c in d:
			if c == ".":
				return True
	return False

def handle_board(case_count,b):
	# print "handling board", b
	if check_board(b):
		# print "board is good"
		
		xwin = check_sym_win(b,"X")
		owin = check_sym_win(b,"O")
		if xwin == True and owin == True:
			msg = "Draw"
		if xwin == True and owin == False:
			msg = "X won"
		if xwin == False and owin == True:
			msg = "O won"
		if xwin == False and owin == False:
			if check_incomplete(b):
				msg = "Game has not completed"
			else:
				msg = "Draw"
	
		print "Case #%s: %s" % (case_count, msg)
		
	else:
		print "board is bad"

case_count = 1
tmp_board = []
i  = 0
for d in data:
	if len(data[i])==0:
		handle_board(case_count, tmp_board)
		tmp_board = []
		case_count = case_count + 1
	else:
		tmp_board.append(data[i])

	i = i + 1
# handle last board

if len(tmp_board)>0:
	handle_board(case_count, tmp_board)

