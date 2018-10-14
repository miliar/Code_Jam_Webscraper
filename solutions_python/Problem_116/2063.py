#!/usr/bin/python

def sayIt(line):
	if line.count('X') == 4 or line.count('X') == 3 and line.count('T') == 1:
		print "X won"
		return True
	elif line.count('O') == 4  or line.count('O') == 3 and line.count('T') == 1:
		print "O won"
		return True
	else: return False

def whoWon(tic):
	solved = False
	points = 0
	i,j=3,0
	ldiag = ""
	rdiag = ""
	for line in tic:
		points += line.count('.')
		solved = sayIt(line)
		#check diagonale 
		if solved:
			return True
		solved = sayIt(tic[0][j]+tic[1][j]+tic[2][j]+tic[3][j])
		if solved:
			return True
		ldiag += line[i]
		i-=1
		rdiag += line[j]
		j+=1
	if not solved:
		solved = sayIt(ldiag)
	if not solved:
		solved = sayIt(rdiag)
	if points == 0 and not solved:
		print "Draw"
	elif points > 0 and not solved:
		print "Game has not completed"

f = file("A-large.in")

cases = int(f.readline())
n=cases
tic = []
while cases :
	print "Case #{0}:".format(n-cases+1),
	
	for i in range(1,5):
		tic.append(f.readline().strip())
	whoWon(tic)
	f.readline()
	tic = []
	cases-=1

