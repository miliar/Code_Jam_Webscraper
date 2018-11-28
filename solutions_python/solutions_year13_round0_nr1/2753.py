#!/usr/env/bin/ python

source = 'A-small-attempt2.in'

def tomek(filename):
	f=open(source)
	n = int(f.readline())
	i = 1
	while i<n+1:
		line = f.readline()
		first = list(line)
		
		
		next = f.readline()
		second = list(next)
		
		next2=f.readline()
		third = list(next2)
		next3 = f.readline()
		fourth = list(next3)

		board = [first, second,third,fourth]

		result = find_winner(board)
		print "Case #" + str(i) + ": " + result 
		next4 = f.readline()
		
		i+= 1


def find_winner(board):
	#check rows
	dotcount = 0
	Xwin = 0
	Owin = 0
	rowdot = 0
	for i in range(0,4):
		Ocount = 0
		Xcount = 0
		for j in range(0,4):
			if board[i][j] == 'O':
				Ocount += 1
			if board[i][j] == 'X':
				Xcount += 1
			if board[i][j] == '.':
				dotcount += 1
				rowdot += 1

		if Xcount == 3 and Ocount != 1 and rowdot != 1:

			Xwin += 1
			return 'X won'
		if Xcount == 4:
			Xwin += 1
			return 'X won'
		if Ocount == 3 and Xcount != 1 and rowdot != 1:
			Owin += 1
			
			return 'O won'
		if Ocount == 4:
			Owin += 1
			return 'O won'
	#check columns
	for i in range(0,4):
		Ocount = 0
		coldot = 0
		Xcount = 0
		for j in range(0,4):
			if board[j][i] == 'O':
				Ocount +=1
			if board[j][i] == 'X':
				Xcount +=1
			if board[j][i] == '.':
				dotcount += 1
				coldot += 1
		if Xcount == 3 and Ocount != 1 and coldot !=1:
			Xwin += 1
			return 'X won'
		if Xcount == 4:
			Xwin += 1
			return 'X won'
		if Ocount == 3 and Xcount != 1 and coldot !=1:
			Owin += 1	
			return 'O won'
		if Ocount == 4:
			Owin += 1		
			return 'O won'
	
	#check diagonals
	Ocount = 0
	Xcount = 0
	diagdot = 0
	for i in range(0,4):
		if board[i][i] == 'O':
			Ocount += 1
		if board[i][i] == 'X':
			Xcount += 1
		if board [i][i] == '.':
			diagdot += 1
	if Xcount == 3 and Ocount != 1 and diagdot != 1:
			Xwin += 1
			return 'X won'
	if Xcount == 4:
			Xwin += 1
			return 'X won'
	if Ocount == 3 and Xcount != 1 and diagdot != 1:
			Owin += 1	
			return 'O won'
	if Ocount == 4:
			Owin += 1
			return 'O won'		
	Ocount = 0
	Xcount = 0
	diagdot = 0
	for j in range(0,4):
		if board[j][3-j] == 'O':
			Ocount +=1
		if board[j][3-j] == 'X':
			Xcount +=1
		if board[j][3-j] == '.':
			diagdot +=1
	if Xcount == 3 and Ocount != 1 and diagdot != 1:
		Xwin += 1
		return 'X won'
	if Xcount == 4:
		Xwin += 1
		return 'X won'
	if Ocount == 3 and Xcount != 1 and diagdot!= 1:
		Owin += 1	
		return 'O won'
	if Ocount == 4:
		return 'O won'
		Owin += 1		
		
	if dotcount == 0 and Xwin == 0 and Owin == 0:
		return "Draw"
	if dotcount != 0 and Xwin == 0 and Owin == 0:
		return "Game has not completed"

tomek(source)		