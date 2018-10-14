import sys
t = int(sys.stdin.readline())
for i in range(0,t):
	line = sys.stdin.readline().split(" ")
	n = int(line[0])
	k = int(line[1])
	board = []
	for p in range(0,n):
		board.append(sys.stdin.readline())
		newline = board[p].replace(".","")
		for q in range(0,n-len(newline)+1):
			newline = "."+newline
		board[p] = newline
	rwin = False
	bwin = False
	for p in range(0,n):
		count = 0
		last = '.'
		for q in range(0,n):
			if (board[p][q]==last):
				count = count+1
			else:
				count = 1
				last = board[p][q]
			if (count>=k):
				if (last=='R'):
					rwin = True
				elif (last=='B'):
					bwin = True
	for p in range(0,n):
		count = 0
		last = '.'
		for q in range(0,n):
			if (board[q][p]==last):
				count = count+1
			else:
				count = 1
				last = board[q][p]
			if (count>=k):
				if (last=='R'):
					rwin = True
				elif (last=='B'):
					bwin = True
	for p in range(0,n):
		count = 0
		last = '.'
		for q in range(0,n-p):
			if (board[p+q][q]==last):
				count = count+1
			else:
				count = 1
				last = board[p+q][q]
			if (count>=k):
				if (last=='R'):
					rwin = True
				elif (last=='B'):
					bwin = True
	for p in range(0,n):
		count = 0
		last = '.'
		for q in range(0,n-p):
			if (board[q][p+q]==last):
				count = count+1
			else:
				count = 1
				last = board[q][p+q]
			if (count>=k):
				if (last=='R'):
					rwin = True
				elif (last=='B'):
					bwin = True
	for p in range(0,n):
		count = 0
		last = '.'
		for q in range(0,n-p):
			if (board[n-(p+q)-1][q]==last):
				count = count+1
			else:
				count = 1
				last = board[n-(p+q)-1][q]
			if (count>=k):
				if (last=='R'):
					rwin = True
				elif (last=='B'):
					bwin = True
	for p in range(0,n):
		count = 0
		last = '.'
		for q in range(0,n-p):
			if (board[n-q-1][p+q]==last):
				count = count+1
			else:
				count = 1
				last = board[n-q-1][p+q]
			if (count>=k):
				if (last=='R'):
					rwin = True
				elif (last=='B'):
					bwin = True
	

	print "Case #"+str(i+1)+":",
	if (rwin and bwin):
		print "Both"
	elif (rwin):
		print "Red"
	elif (bwin):
		print "Blue"
	else:
		print "Neither"
