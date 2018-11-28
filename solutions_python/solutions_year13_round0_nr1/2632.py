import fileinput
test_case = 1
count = 0
Matrix = [[0 for x in xrange(4)] for x in xrange(4)]
xwon = False
owon = False
nfin = False
draw = False
sentence = ""
def countCharLst(char, lst):
	x = 0
	result = 0
	while x < len(lst):
		if lst[x] == char:
			result = result + 1			
		x  = x + 1
	return result
def countCharLstByPos(char, lst, pos):
	x = 0
	result = 0
	while x < 4:
		if lst[x][pos] == char:
			result = result + 1
		x = x + 1
	return result
def countDiag1(lst,char):
	result = 0
	if lst[0][0] == char:
		result = result + 1
	if lst[1][1] == char:
		result = result + 1			
	if lst[2][2] == char:
		result = result + 1
	if lst[3][3] == char:
		result = result + 1
	return result
def countDiag2(lst,char):
	result = 0
	if lst[0][3] == char:
		result = result + 1
	if lst[1][2] == char:
		result = result + 1
	if lst[2][1] == char:
		result = result  + 1
	if lst[3][0] == char:
		result = result + 1
	return result
for line in fileinput.input():
	if not fileinput.isfirstline() and line <> "" and line <> "\n":		
		x = 0		
		while x <= 3:
			Matrix[count][x] = line[x]									
			x = x + 1		
		#print Matrix
		count = count + 1
		if count == 4:
			y = 0
			while y < 4:
				if countCharLst('X', Matrix[y]) == 4 or (countCharLst('X', Matrix[y]) == 3 and countCharLst('T', Matrix[y]) == 1):
					xwon = True
				elif countCharLstByPos('X', Matrix, y) == 4 or (countCharLstByPos('X',Matrix,y) == 3 and countCharLstByPos('T',Matrix,y) == 1):
					xwon = True 
				elif countDiag1(Matrix,'X') == 4 or (countDiag1(Matrix,'X') == 3 and countDiag1(Matrix,'T') == 1):
					xwon = True
				elif countDiag2(Matrix,'X') == 4 or (countDiag2(Matrix,'X') == 3 and countDiag2(Matrix,'T') == 1):
					xwon = True
				elif countCharLst('O', Matrix[y]) == 4 or (countCharLst('O', Matrix[y]) == 3 and countCharLst('T', Matrix[y]) == 1):
					owon = True
				elif countCharLstByPos('O', Matrix, y) == 4 or (countCharLstByPos('O',Matrix,y) == 3 and countCharLstByPos('T',Matrix,y) == 1):
					owon = True
				elif countDiag1(Matrix,'O') == 4 or (countDiag1(Matrix,'O') == 3 and countDiag1(Matrix,'T') == 1):
					owon = True
				elif countDiag2(Matrix,'O') == 4 or (countDiag2(Matrix,'O') == 3 and countDiag2(Matrix,'T') == 1):
					owon = True				 
				y = y + 1
			
			if owon == False and xwon == False:
				z = 0
				j = 0
				while z < 4:
					j = j + countCharLst('.',Matrix[z])
					z = z + 1
				if j == 0:
					draw = True
				else:
					nfin = True
			if xwon == True:
				sentence = "X won"
			if owon == True:
				sentence = "O won"
			if draw == True:
				sentence = "Draw"
			if nfin == True:
				sentence = "Game has not completed"
			#print sentence
			Matrix = [[0 for x in xrange(4)] for x in xrange(4)]
			count = 0
			print "Case #%d: %s" % (test_case, sentence)
			test_case = test_case + 1
			xwon = False
			owon = False		
			draw = False
			nfin = False
			sentence = ""
	#print Matrix[3]
	
