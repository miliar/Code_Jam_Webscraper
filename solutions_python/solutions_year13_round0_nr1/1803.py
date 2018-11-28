f = open('A-large.in')
f=f.read().splitlines()
cases = int(f[0]) # number of cases in the file
linesPerCase = 5 # lines per each case

ans=""
case = 0
for i in range(1, cases*linesPerCase, linesPerCase):
	case += 1
	board = [ map(ord, f[i+x]) for x in range(4)]
	openspace = False
	winner = False
	for line in board: # horizontal
		if 46 in line: # if there is an open space
			openspace = True
		if (sum(line) == 352 or sum(line)== 348 )and (not winner):
			ans += "Case #" + str(case) + ": X won\n"
			winner = True
			break
		elif (sum(line) == 316 or sum(line)== 321) and (not winner):
			ans += "Case #" + str(case) + ": O won\n"
			winner = True
			break
	if not winner:
		for i in range(4): # vertical
			x = board[0][i]+board[1][i]+board[2][i]+board[3][i]
			if (x == 352 or x == 348) and not winner:
				ans += "Case #" + str(case) + ": X won\n"
				winner = True
				break
			elif (x == 316 or x== 321) and not winner:
				ans += "Case #" + str(case) + ": O won\n"
				winner = True
				break
	# diag
	if not winner:
		diagr = board[0][0]+board[1][1]+board[2][2]+board[3][3] # diagonal down & right
		diagl = board[0][3]+board[1][2]+board[2][1]+board[3][0] # diagonal down & left
		if diagr == 352 or diagr == 348 or diagl == 352 or diagl == 348 and not winner:
			ans += "Case #" + str(case) + ": X won\n"
			winner = True
		elif diagr == 316 or diagr== 321 or diagl == 316 or diagl == 321 and not winner:
			ans += "Case #" + str(case) + ": O won\n"
			winner = True
		if (not winner) and openspace:
			ans+="Case #" + str(case) + ": Game has not completed\n"
		if (not winner) and (not openspace):
			ans+="Case #" + str(case) + ": Draw\n"
	

a=open('large.txt','w')
a.write(ans)
