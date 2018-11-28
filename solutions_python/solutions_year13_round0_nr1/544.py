import sys,os

matrix = [[0 for x in range(4)] for x in range(4)]

def wonX(line):
	if line == "TXXX":
		return True
	if line == "XXXX":
		return True
	return False

def wonO(line):
	if line == "OOOT":
		return True
	if line == "OOOO":
		return True
	return False

def readInput(filename):
	global matrix
	linia = 0
	coloana = 0

	f = open(filename)
	lines = f.readlines()

	nrMat = int(lines[0])
	tryMat = 1
	for line in lines[1:]:

		if tryMat > nrMat:
			return

		line = line.strip()
		if line == "" or linia == 4: # acel linia == 4 e pt ultima matrice
			#print "Am terminat cu matricea, calculam rezultatul:"
			#print matrix
			print "Case #%d:" % tryMat,
			findSolution(matrix)

			linia = 0
			tryMat += 1
			continue

		coloana = 0
		for c in line:
			matrix[linia][coloana] = c
			coloana += 1
		linia += 1
	f.close()
		

def findSolution(matrix):
#	for line in matrix:
#		print ">>",line

	ll = []
	# get lines	
	for i in range(4):
		r = ""
		for j in range(4):
			r = r + matrix[i][j]
		ll.append( "".join(sorted(list(r))) )
	# get columns
	for i in range(4):
		r = ""
		for j in range(4):
			r = r + matrix[j][i]
		ll.append( "".join(sorted(list(r))) )
	# get diagonal 1
	r = ""
	for i in range(4):
		r = r + matrix[i][i]
	ll.append( "".join(sorted(list(r))) )
	# get diagonal 2
	r = ""
	for i in range(4):
		r = r + matrix[i][3-i]
	ll.append( "".join(sorted(list(r))) )

	for l in ll:
		if wonX(l):
			print "X won"
			return
		if wonO(l):
			print "O won"
			return
	
	# aci decid daca e draw sau not completed		
	for i in range(4):
		for j in range(4):
			if matrix[i][j] == ".":
				print "Game has not completed"
				return
	print "Draw"
	return

readInput("input.txt")                                      

	