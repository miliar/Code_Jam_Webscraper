
def won(who,game):
	for i in range(0,4):
		wonRow = True
		wonColumn = True
		wonDiag1 = True
		wonDiag2 = True
		for j in range(0,4):
			if game[i][j] != who and game[i][j] != 'T':
				wonRow = False
			if game[j][i] != who and game[j][i] != 'T':
				wonColumn = False
			if game[j][j] != who and game[j][j] != 'T':
				wonDiag1 = False
			if game[3-j][j] != who and game[3-j][j] != 'T':
				wonDiag2 = False
		if wonRow or wonColumn or wonDiag1 or wonDiag2:
			return True


num = int(raw_input())

games = []

for i in range(0,num) :
	games.append([])
	for j in range(0,4) :
		games[i].append([])
		line = raw_input()
		for k in range(0,4) :
			games[i][j].append(line[k])
	if i != num:
		raw_input()
	else:
		print ''

for i in range(0,num):
	wonX = won('X',games[i])
	wonO = won('O',games[i])
	if wonX:
		print "Case #{}: X won".format(i+1)
	if wonO:
		print "Case #{}: O won".format(i+1)
	if ( not wonX ) and ( not wonO ):
		finished = True
		for l in games[i]:
			for c in l:
				if c == '.':
					finished = False
		if finished:
			print "Case #{}: Draw".format(i+1)
		else:
			print "Case #{}: Game has not completed".format(i+1)
