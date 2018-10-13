#!/usr/bin/env python

f = open('A-small-attempt3.in', 'r')
count = int(f.readline())
counter = 0

def board(iterator, size):
	yield tuple(next(iterator) for _ in range(size))
while counter < count:
	counter = counter + 1
	for line1, line2, line3, line4, line5 in board(f, size=5):
		columnOne = line1[0] + line2[0] + line3[0] + line4[0]
		columnTwo = line1[1] + line2[1] + line3[1] + line4[1]
		columnThree = line1[2] + line2[2] + line3[2] + line4[2]
		columnFour = line1[3] + line2[3] + line3[3] + line4[3]
		diagonalOne = line1[0] + line2[1] + line3[2] + line4[3]
		diagonalTwo = line1[3] + line2[2] + line3[1] + line4[0]
		lines = line1 + line2 + line3 + line4
		
		if ("XXXX" in columnOne) or \
		   ("XXXX" in lines) or \
		   ("XXXX" in columnTwo) or \
		   ("XXXX" in columnThree) or \
		   ("XXXX" in columnFour) or \
		   ("XXXX" in diagonalOne) or \
		   ("XXXX" in diagonalTwo) or \
		   ("TXXX" in columnOne) or \
		   ("TXXX" in lines) or \
		   ("TXXX" in columnTwo) or \
		   ("TXXX" in columnThree) or \
		   ("TXXX" in columnFour) or \
		   ("TXXX" in diagonalOne) or \
		   ("TXXX" in diagonalTwo) or \
		   ("XXXT" in columnOne) or \
		   ("XXXT" in lines) or \
		   ("XXXT" in columnTwo) or \
		   ("XXXT" in columnThree) or \
		   ("XXXT" in columnFour) or \
		   ("XXXT" in diagonalOne) or \
		   ("XXXT" in diagonalTwo):
			
			print "Case #" + str(counter) + ": X won"
		
		elif ("OOOO" in columnOne) or \
		   ("OOOO" in lines) or \
		   ("OOOO" in columnTwo) or \
		   ("OOOO" in columnThree) or \
		   ("OOOO" in columnFour) or \
		   ("OOOO" in diagonalOne) or \
		   ("OOOO" in diagonalTwo) or \
		   ("TOOO" in columnOne) or \
		   ("TOOO" in lines) or \
		   ("TOOO" in columnTwo) or \
		   ("TOOO" in columnThree) or \
		   ("TOOO" in columnFour) or \
		   ("TOOO" in diagonalOne) or \
		   ("TOOO" in diagonalTwo) or \
		   ("OOOT" in columnOne) or \
		   ("OOOT" in lines) or \
		   ("OOOT" in columnTwo) or \
		   ("OOOT" in columnThree) or \
		   ("OOOT" in columnFour) or \
		   ("OOOT" in diagonalOne) or \
		   ("OOOT" in diagonalTwo):

		   	print "Case #" + str(counter) + ": O won"
		
		elif ("." in columnOne) or \
		   ("." in lines) or \
		   ("." in columnTwo) or \
		   ("." in columnThree) or \
		   ("." in columnFour) or \
		   ("." in diagonalOne) or \
		   ("." in diagonalTwo):
			
			print "Case #" + str(counter) + ": Game has not completed"

		else:
			print "Case #" + str(counter) + ": Draw"