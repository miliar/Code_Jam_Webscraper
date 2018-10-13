

import sys

def count(myList):
	numX = 0
	numO = 0
	numT = 0

	for i in myList:
		if i == 'X': numX+=1
		if i == 'O': numO+=1
		if i == 'T': numT+=1

	if numX + numT == 4 and numT <= 1: return 'X'
	elif numO + numT == 4 and numT <= 1: return 'O'
	else: return 'R'

def findWinner(gl):
	if count((gl[0], gl[1], gl[2], gl[3])) == 'X': return 'X'
	if count((gl[0], gl[1], gl[2], gl[3])) == 'O': return 'O'

	if count((gl[4], gl[5], gl[6], gl[7])) == 'X': return 'X'
	if count((gl[4], gl[5], gl[6], gl[7])) == 'O': return 'O'

	if count((gl[8], gl[9], gl[10], gl[11])) == 'X': return 'X'
	if count((gl[8], gl[9], gl[10], gl[11])) == 'O': return 'O'

	if count((gl[12], gl[13], gl[14], gl[15])) == 'X': return 'X'
	if count((gl[12], gl[13], gl[14], gl[15])) == 'O': return 'O'

	if count((gl[0], gl[4], gl[8], gl[12])) == 'X': return 'X'
	if count((gl[0], gl[4], gl[8], gl[12])) == 'O': return 'O'

	if count((gl[1], gl[5], gl[9], gl[13])) == 'X': return 'X'
	if count((gl[1], gl[5], gl[9], gl[13])) == 'O': return 'O'

	if count((gl[2], gl[6], gl[10], gl[14])) == 'X': return 'X'
	if count((gl[2], gl[6], gl[10], gl[14])) == 'O': return 'O'

	if count((gl[3], gl[7], gl[11], gl[15])) == 'X': return 'X'
	if count((gl[3], gl[7], gl[11], gl[15])) == 'O': return 'O'

	if count((gl[0], gl[5], gl[10], gl[15])) == 'X': return 'X'
	if count((gl[0], gl[5], gl[10], gl[15])) == 'O': return 'O'

	if count((gl[3], gl[6], gl[9], gl[12])) == 'X': return 'X'
	if count((gl[3], gl[6], gl[9], gl[12])) == 'O': return 'O'

	return 'R'

def findDot(gl):
	for r in gl:
		if r == '.': return True
	return False

def init():

	filename = sys.argv[1]

	try:

		fp = open(filename, "r")

	except IOError, e:

		print 'Opening filename does not exist!'
		sys.exit(0)

	else:

		# Get the size of test cases
		num = fp.readline()

		case = 1

		while 1:

			if case <= int(num):

				gridList = ()

				for x in range (0, 4):
					line = fp.readline()
					(a, b, c, d) = line[0:4]
					gridList = gridList + (a, b, c, d)

				#Print the tuple for debugging
				#print gridList

				result = findWinner(gridList)
				if (result == 'X'):
					print "Case #%d: X won" % case
				elif (result == 'O'):
					print "Case #%d: O won" % case
				else:
					
					if (findDot(gridList)):
						print "Case #%d: Game has not completed" % case
					else:
						print "Case #%d: Draw" % case

				if case != num:
					line = fp.readline()

				case += 1

				del gridList

			else:
				break


		#print count(gridList)

init()

