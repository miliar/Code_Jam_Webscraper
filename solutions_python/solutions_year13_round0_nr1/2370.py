#!/usr/bin/python
import re
def check_complete(matrix):
	periods = 0
	for i in range(4):
		for j in range(4):
			if matrix[i][j] is ".":
				periods += 1
			
	return periods
	
def check_horizontal(matrix):
	pointsO = 0
	pointsX = 0
	periods = 0
	winner = False
	for i in range(4):
		for j in range(4):
			if matrix[i][j] is "O":
				pointsO += 1
			elif matrix[i][j] is "X":
				pointsX += 1
			elif matrix[i][j] is "T":
				pointsX += 1
				pointsO += 1
			elif matrix[i][j] is ".":
				periods += 1
		if pointsO == 4:
			print "Case #"+str(case+1)+": O won"
			winner = True
			break
		elif pointsX == 4:
			print "Case #"+str(case+1)+": X won"
			winner = True
			break
		pointsO = 0
		pointsX = 0
	return winner
	


def check_vertical(matrix):
	pointsO = 0
	pointsX = 0
	periods = 0
	winner = False
	
	for j in range(4):
		for i in range(4):
			if matrix[i][j] is "O":
				pointsO += 1
			elif matrix[i][j] is "X":
				pointsX += 1
			elif matrix[i][j] is "T":
				pointsX += 1
				pointsO += 1
			elif matrix[i][j] is ".":
				periods += 1
		if pointsO == 4:
			print "Case #"+str(case+1)+": O won"
			winner = True
			break
		elif pointsX == 4:
			print "Case #"+str(case+1)+": X won"
			winner = True
			break
		pointsO = 0
		pointsX = 0
	return winner


def check_diagonal1(matrix):
	pointsO = 0
	pointsX = 0
	periods = 0
	winner = False
	
	for i in range(4):
		if matrix[i][i] is "O":
			pointsO += 1
		elif matrix[i][i] is "X":
			pointsX += 1
		elif matrix[i][i] is "T":
			pointsX += 1
			pointsO += 1
		elif matrix[i][i] is ".":
			periods += 1
		if pointsO == 4:
			print "Case #"+str(case+1)+": O won"
			winner = True
			break
		elif pointsX == 4:
			print "Case #"+str(case+1)+": X won"
			winner = True
			break
	return winner
	
def check_diagonal2(matrix):
	
	pointsO = 0
	pointsX = 0
	periods = 0
	winner = False
	for i in range(4):
		if matrix[i][(len(matrix[i])-1)-i] is "O":
			pointsO += 1
		elif matrix[i][(len(matrix[i])-1)-i] is "X":
			pointsX += 1
		elif matrix[i][(len(matrix[i])-1)-i] is "T":
			pointsX += 1
			pointsO += 1
		elif matrix[i][(len(matrix[i])-1)-i] is ".":
			periods += 1
		if pointsO == 4:
			print "Case #"+str(case+1)+": O won"
			winner = True
			break
		elif pointsX == 4:
			print "Case #"+str(case+1)+": X won"
			winner = True
			break
	return winner
	
f = open("A-large.in", "r")
cases = int(f.readline())

for case in range(cases):
	matrix =  [[0 for x in xrange(4)] for x in xrange(4)] 
	for i in range(4):
		line = f.readline()
		linea = list(line)
		for j in range(4):
			matrix[i][j] = linea[j]
			
	#print matrix
	winner = False
	
	winner = check_horizontal(matrix)
	if winner == False:
		winner = check_vertical(matrix)
	if winner == False:
		winner = check_diagonal1(matrix)
	if winner == False:
		winner = check_diagonal2(matrix)
	
	if winner == False:
		periods = check_complete(matrix)
		if periods > 0:
			print "Case #"+str(case+1)+": Game has not completed"
		else:
			print "Case #"+str(case+1)+": Draw"
	
	f.readline()

f.close()