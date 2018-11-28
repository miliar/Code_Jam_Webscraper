#! /Library/Frameworks/Python.framework/Versions/Current/bin/python

T = int(raw_input())

for t in range(T):

	s = [raw_input()[:4] for i in range(4)]
	if (t < T-1):
		raw_input()

	# horizontal
	for i in range(4):
		Xwon = True
		Owon = True
		for j in range(4):
			if ((s[i][j] != 'X') and (s[i][j] != 'T')):
				Xwon = False
			if ((s[i][j] != 'O') and (s[i][j] != 'T')):
				Owon = False
		if (Xwon or Owon):
			break

	# vertical
	if (not(Xwon) and not(Owon)):
		for j in range(4):
			Xwon = True
			Owon = True
			for i in range(4):
				if ((s[i][j] != 'X') and (s[i][j] != 'T')):
					Xwon = False
				if ((s[i][j] != 'O') and (s[i][j] != 'T')):
					Owon = False
			if (Xwon or Owon):
				break

	# diagonals
	if (not(Xwon) and not(Owon)):
		Xwon = True
		Owon = True
		for i in range(4):
			j = i
			if ((s[i][j] != 'X') and (s[i][j] != 'T')):
				Xwon = False
			if ((s[i][j] != 'O') and (s[i][j] != 'T')):
				Owon = False

	if (not(Xwon) and not(Owon)):
		Xwon = True
		Owon = True
		for i in range(4):
			j = 3-i
			if ((s[i][j] != 'X') and (s[i][j] != 'T')):
				Xwon = False
			if ((s[i][j] != 'O') and (s[i][j] != 'T')):
				Owon = False

	# check for game over
	GameOver = True
	for i in range(4):
		for j in range(4):
			if (s[i][j] == '.'):
				GameOver = False

	print 'Case #' + str(t+1) + ':',
	if Xwon:
		print 'X won'
	elif Owon:
		print 'O won'
	elif GameOver:
		print 'Draw'
	else:
		print 'Game has not completed'