'''Google Code Jam 2013'''
'''Qualification Round'''
'''A. Tic-Tac-Toe-Tomek'''
'''@author ationsong@gmail.com'''

#Passes in a LIST
def checkRow(row):
	if row.count('X') == 4 or (row.count('X') == 3 and (row[0] == 'T' or row[1] == 'T' or row[2] == 'T' or row[3] == 'T')):
		return "X won"
	if row.count('O') == 4 or (row.count('O') == 3 and (row[0] == 'T' or row[1] == 'T' or row[2] == 'T' or row[3] == 'T')):
		return "O won"
	return None

def processFile(name):
	f = open(name, 'r')
	lines = f.readlines()

	out = open('A-Output-Big.txt', 'w')

	T = int(lines[0].split(' ')[0].strip())
	print "Cases:" + str(T)

	i = 1
	case = 1
	while (case <= T ):

		out.write("Case #" + str(case) + ": ")
		#print "Case #" + str(case) + ": "

		# Read one board --cheap and dirty, but it works
		b1 = [lines[i][0], lines[i][1], lines[i][2], lines[i][3]]
		i += 1
		b2 = [lines[i][0], lines[i][1], lines[i][2], lines[i][3]]
		i += 1
		b3 = [lines[i][0], lines[i][1], lines[i][2], lines[i][3]]
		i += 1
		b4 = [lines[i][0], lines[i][1], lines[i][2], lines[i][3]]

		#board = [b1, b2, b3, b4]
		#print board

		##
		## Check horizontal rows
		##
		c1 = checkRow(b1)
		c2 = checkRow(b2)
		c3 = checkRow(b3)
		c4 = checkRow(b4)

		solved = False
		if not c1 == None:
			out.write( c1 )
			solved = True
		elif not c2 == None:
			out.write( c2)
			solved = True
		elif not c3 == None:
			out.write( c3)
			solved = True
		elif not c4 == None:
			out.write( c4)
			solved = True

		if not solved:
			##
			## Check vertical columns
			##
			d1 = checkRow([b1[0], b2[0], b3[0], b4[0]])
			d2 = checkRow([b1[1], b2[1], b3[1], b4[1]])
			d3 = checkRow([b1[2], b2[2], b3[2], b4[2]])
			d4 = checkRow([b1[3], b2[3], b3[3], b4[3]])

			if not d1 == None:
				out.write( d1)
				solved = True
			elif not d2 == None:
				out.write( d2)
				solved = True
			elif not d3 == None:
				out.write( d3)
				solved = True
			elif not d4 == None:
				out.write( d4)
				solved = True

		if not solved:
			##
			## Check diagonals
			##
			e1 = checkRow([b1[0], b2[1], b3[2], b4[3]])
			e2 = checkRow([b1[3], b2[2], b3[1], b4[0]])

			if not e1 == None:
				out.write( e1)
				solved = True
			elif not e2 == None:
				out.write( e2)
				solved = True

		if not solved:
			if b1.count('.') > 0 or b2.count('.') > 0 or b3.count('.') > 0 or b4.count('.') > 0:
				out.write( "Game has not completed")
			else:
				out.write( "Draw")

		out.write("\n")
		i += 2
		case += 1

processFile('A-large.in')