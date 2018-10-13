num=int(input())
for casenum in range(1, num+1):
	board = [input(), input(), input(), input()]
	if casenum < num:
		input()	# seperating empty line

	# translate table
	# sum (3 or 4: X ; 30 or 40: O ; )
	t_num = 0
	x_num = 1
	o_num = 10
	dot_num = 100
	has_space = False

	rowsum = [0, 0, 0, 0]
	clmsum = [0, 0, 0, 0]
	diasum = [0, 0, 0, 0]
	for rownum in range(4):
		for clmnum in range(4):
			if board[rownum][clmnum] == 'X':
				rowsum[rownum] += x_num
				clmsum[clmnum] += x_num
				if rownum == clmnum:
					diasum[0] += x_num
				elif rownum+clmnum == 3:
					diasum[1] += x_num
			elif board[rownum][clmnum] == 'O':
				rowsum[rownum] += o_num
				clmsum[clmnum] += o_num
				if rownum == clmnum:
					diasum[0] += o_num
				elif rownum+clmnum == 3:
					diasum[1] += o_num
			elif board[rownum][clmnum] == '.':
				has_space = True
				rowsum[rownum] += dot_num
				clmsum[clmnum] += dot_num
				if rownum == clmnum:
					diasum[0] += dot_num
				elif rownum+clmnum == 3:
					diasum[1] += dot_num
	who_won = 'T'
	for n in range(4):
		if rowsum[n] == 3 or rowsum[n] == 4 or clmsum[n] == 3 or clmsum[n] == 4 or diasum[n] == 3 or diasum[n] == 4:
			who_won = 'X'
			break
		elif rowsum[n] == 30 or rowsum[n] == 40 or clmsum[n] == 30 or clmsum[n] == 40 or diasum[n] == 30 or diasum[n] == 40:
			who_won = 'O'
			break
	if who_won == 'X':
		print("Case #%d: X won" % casenum)
	elif who_won == 'O':
		print("Case #%d: O won" % casenum)
	elif has_space == True:
		print("Case #%d: Game has not completed" % casenum)
	else:
		print("Case #%d: Draw" % casenum)
