#! /usr/bin/python

def check_board(arr):
	c1 = 0
	c2 = 0
	c3 = 0
	c4 = 0
	r1 = 0
	r2 = 0
	r3 = 0
	r4 = 0
	d1 = 0
	d2 = 0
	
	for i in range(0, 4):
		#row
		c1 += ord(arr[0][i])
		c2 += ord(arr[1][i])
		c3 += ord(arr[2][i])
		c4 += ord(arr[3][i])
		
		#col
		r1 += ord(arr[i][0])
		r2 += ord(arr[i][1])
		r3 += ord(arr[i][2])
		r4 += ord(arr[i][3])
		
		#diag
		d1 += ord(arr[i][i])
		d2 += ord(arr[3-i][i])
	
	x_wins = ord("X")*4
	o_wins = ord("O")*4
	win_set = [r1, r2, r3, r4, c1, c2, c3, c4, d1, d2]
	
	if x_wins in win_set or x_wins-4 in win_set:
		return "X won"
	elif o_wins in win_set or o_wins+5 in win_set:
		return "O won"
	else:
		for r in sq:
			if "." in r:
				return "Game has not completed"
		return "Draw"

ifile = open("A-large.in", "r")

#ignore data not necessary for python fileio
cases = int(ifile.readline())

for i in range(0, cases):
	sq = []
	for j in range(0, 4): #load
		line = ifile.readline().rstrip(" \r\n")
		arr = [ch for ch in line]
		sq.append(arr)
	
	print "Case #" + str(i+1) + ": " + check_board(sq)
	
	ifile.readline()
	

