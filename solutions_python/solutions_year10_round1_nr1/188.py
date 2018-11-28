#!/usr/bin/python2.6
import sys
data = sys.stdin
caseno = int(data.readline())
for case in xrange(1,caseno+1):
	print "Case #%d:"%case,
	N, K = map(int,data.readline().split())
	board = []
	for line in xrange(N):
		board.append(data.readline().strip())	

	newboard = []
	for line in board:
		pieceseen = False
		newline = []
		for spot in xrange(len(line)):
			if line[spot] == 'R' or line[spot] == 'B':
				newline.append(line[spot])
		newline.reverse()
		while len(newline) < N:
			newline.append('.')
		newline.reverse()
		newboard.append(newline)
	
	Red = False
	Blue = False
	#count horizontal
	for x in xrange(N):
		Kcount = K -1
		last = None
		for y in xrange(N):
			if last == newboard[x][y] and last != '.':
				Kcount = Kcount -1
			else:
				Kcount = K -1
			last = newboard[x][y]
			if Kcount == 0:
				if last == 'B':
					Blue = True
				else:
					Red = True

	#count vertical
	for x in xrange(N):
		Kcount = K -1
		last = None
		for y in xrange(N):
			if last == newboard[y][x] and last != '.':
				Kcount = Kcount -1
			else:
				Kcount = K -1
			last = newboard[y][x]
			if Kcount == 0:
				if last == 'B':
					Blue = True
				else:
					Red = True

	#count diaginal
	for x in xrange(1,N+1):
		Kcount = K -1
		last = None
		A = range(x)
		B = range(x)
		B.reverse()
		for y,z in zip(A, B):
			if last == newboard[y][z] and last != '.':
				Kcount = Kcount -1
			else:
				Kcount = K -1
			last = newboard[y][z]
			if Kcount == 0:
				if last == 'B':
					Blue = True
				else:
					Red = True
		Kcount = K -1
		last = None
		A = range(x, N)
		B = range(x, N)
		B.reverse()
		for y,z in zip(B, A):
			if last == newboard[y][z] and last != '.':
				Kcount = Kcount -1
			else:
				Kcount = K -1
			last = newboard[y][z]
			if Kcount == 0:
				if last == 'B':
					Blue = True
				else:
					Red = True

	#count diaginal
	for x in xrange(0,N+1):
		A = range(x)
		B = range(x)
		C = range(1,x)
		searchpat = [zip(A, A), zip(C, B), zip(B, C)]
		for line in searchpat:
			Kcount = K -1
			last = None
			for y,z in line:
				if last == newboard[z][y] and last != '.':
					Kcount = Kcount -1
				else:
					Kcount = K -1
				last = newboard[z][y]
				if Kcount == 0:
					if last == 'B':
						Blue = True
					else:
						Red = True

	if Red and Blue: print "Both"
	elif Red: print "Red"
	elif Blue: print "Blue"
	else: print "Neither"
