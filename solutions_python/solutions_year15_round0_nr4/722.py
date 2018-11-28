text = open("/Users/cameronfranz/Documents/Learning/Projects/Code Jam/2015/D - Ominoes/D-small-attempt0.in")
numCases = int(text.readline())

#use numpy
import math

def ominoBoxes(n):    
   	s1 = reduce(list.__add__, ([[n-i, i+1]] for i in range(0,n)))
	s2 = reduce(list.__add__, ([[n-i, 1+int(math.ceil(i/float(n-i)))]] for i in range(0,n)))
	uniques = [list(x) for x in set(tuple(x) for x in (s1+s2))]
	return (uniques)

for i in xrange(numCases):	
	line = text.readline().split()
	omino = int(line[0])
	gridX = int(line[2])
	gridY = int(line[1])
	gridSize = gridX * gridY
	winner = "GABRIEL"

	ominoDims = ominoBoxes(omino)
	
	for j in range(len(ominoDims)):
		x = ominoDims[j][0]
		y = ominoDims[j][1]
		
		if((x > gridX or y>gridY) and (x > gridY or y>gridX)):
			winner = "RICHARD"
		if(x == gridX):
			if((gridSize-omino)%omino!=0):
				winner = "RICHARD"
		elif(y == gridY):
			if((gridSize-omino)%omino!=0):
				winner = "RICHARD"
								
	if(gridSize % omino != 0):
		winner = "RICHARD"
			
	print "Case #" + str(i+1) + ": " + str(winner)

