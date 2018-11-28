import sys

for rc in xrange(1, int(sys.stdin.readline())+1):
	gc = True
	t = []
	n = 4
	winword = None
	for i in xrange(n):
		t.append(sys.stdin.readline())
	sys.stdin.readline()
	#Check from row to row
	for r in xrange(n):
		go = t[r][0]
		if go == 'T':
			go = t[r][1]
		if go == '.':
			gc = False
			continue
		for c in xrange(n):
			if t[r][c] == go or t[r][c] == 'T':
				continue
			if t[r][c] == ".":
				gc = False
			break
		if c == n-1:
			if t[r][c] == go or t[r][c] == "T":
				winword = go +" won"
				break
	if winword is not None:
		print 'Case #%d: %s' %(rc, winword)
		continue
	#Check column to column
	for c in xrange(n):
		go = t[0][c]
		if go == 'T':
			go = t[1][c]
		if go == '.':
			gc = False
			continue
		for r in xrange(n):
			if t[r][c] == go or t[r][c] == 'T':
				continue
			else:
				break
		if r == n-1:
			if t[r][c] == go or t[r][c] == "T":
				winword = go + " won"
				break
	if winword is not None:
		print 'Case #%d: %s' %(rc, winword)
		continue
	#Check from right-top to left-bottom
	if t[0][0] != '.':
		go = t[0][0]
		if go == 'T':
			go = t[1][1]
		for i in xrange(n):
			if t[i][i] == go or t[i][i] == "T":
				continue
			else:
				break
		if i == n-1:
			if t[i][i] == go or t[i][i] == "T":
				winword = go + " won"
				print 'Case #%d: %s' %(rc, winword)
				continue
	#Check from right-bottm to left-top
	if t[n-1][0] != ".":
		go = t[n-1][0]
		if go == 'T':
			go = t[n-2][1]
		for i in xrange(n):
			if t[n-1-i][i] == go or t[n-1-i][i] == "T":
				continue
			else:
				break
		if i == n-1:
			if t[0][i] == go or t[0][i] == "T":
				winword = go + " won"
				print 'Case #%d: %s' %(rc, winword)
				continue
	if gc:
		print 'Case #%d: %s' %(rc, "Draw")
	else:
		print 'Case #%d: %s' %(rc, "Game has not completed")


