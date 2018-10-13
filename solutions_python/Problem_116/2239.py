lines = [line.rstrip('\n') for line in open('sample.in')]

cases = int(lines[0])

boards = []

lines = [x for x in lines if x != ""]
lines.pop(0)

case_number = 0
for x in range(0, len(lines), 4):
	case_number += 1

	board = [lines[x], lines[x + 1], lines[x + 2], lines[x + 3]]
	str_board = ' '.join(board)

	x_list = ['X', 'T']
	o_list = ['O', 'T']

	if board[0][0] in x_list and board[1][1] in x_list and board[2][2]  in x_list and board[3][3] in x_list:
		print("Case #%s: X won" % case_number)
		continue

	if board[0][3] in x_list and board[1][2] in x_list and board[2][1]  in x_list and board[3][0] in x_list:
		print("Case #%s: X won" % case_number)
		continue

	if board[0][0] in o_list and board[1][1] in o_list and board[2][2]  in o_list and board[3][3] in o_list:
		print("Case #%s: O won" % case_number)
		continue

	if board[0][3] in o_list and board[1][2] in o_list and board[2][1]  in o_list and board[3][0] in o_list:
		print("Case #%s: O won" % case_number)
		continue

	if 'XXXX' in str_board or 'XXXT' in str_board or 'XXTX' in str_board or 'XTXX' in str_board or 'TXXX' in str_board:
		print("Case #%s: X won" % case_number)
		continue

	if 'OOOO' in str_board or 'OOOT' in str_board or 'OOTO' in str_board or 'OTOO' in str_board or 'TOOO' in str_board:
		print("Case #%s: O won" % case_number)
		continue

	success = False
	for a in range(4):
		if board[0][a] in x_list and board[1][a] in x_list and board[2][a] in x_list and board[3][a] in x_list:
			print("Case #%s: X won" % case_number)
			success = True
			break
		if board[0][a] in o_list and board[1][a] in o_list and board[2][a] in o_list and board[3][a] in o_list:
			print("Case #%s: O won" % case_number)
			success = True
			break
	if success == True:
		continue

	if '.' in str_board:
		print("Case #%s: Game has not completed" % case_number)
		continue
	else:
		print("Case #%s: Draw" % case_number)
		continue