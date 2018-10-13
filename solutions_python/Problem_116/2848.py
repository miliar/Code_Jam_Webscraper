import sys

xBoardH = [0,0,0,0]
xBoardV = [0,0,0,0]
xBoardS1 = 0
xBoardS2 = 0
yBoardH = [0,0,0,0]
yBoardV = [0,0,0,0]
yBoardS1 = 0
yBoardS2 = 0
empty = 0

def loadboard(file):
	global xBoardS1
	global xBoardS2
	global yBoardS1
	global yBoardS2
	global empty

	for i in range(0,4):
		line = file.readline()
		for j in range(0,4):
			
			if line[j] == "X" or line[j] == "T":
				xHVal = xBoardH[i]
				xHVal = xHVal | (1 << (3 - j))
				xBoardH[i] = xHVal

				xVVal = xBoardV[j]
				xVVal = xVVal | (1 << (3 - i))
				xBoardV[j] = xVVal

			if line[j] == "O" or line[j] == "T":
				yHVal = yBoardH[i]
				yHVal = yHVal | (1 << (3 - j))
				yBoardH[i] = yHVal

				yVVal = yBoardV[j]
				yVVal = yVVal | (1 << (3 - i))
				yBoardV[j] = yVVal

			if line[j] == ".":
				empty = 1

			if i == j:
				if line[j] == "X" or line[j] == "T":
					xBoardS1 = xBoardS1 | (1 << (3 - i))

				if line[j] == "O" or line[j] == "T":
					yBoardS1 = yBoardS1 | (1 << (3 - i))
				
			if (3 - i) == j:
				if line[j] == "X" or line[j] == "T":
					xBoardS2 = xBoardS2 | (1 << (3 - i))

				if line[j] == "O" or line[j] == "T":
					yBoardS2 = yBoardS2 | (1 << (3 - i))


argvs = sys.argv

file = open(argvs[1])

datacount = int(file.readline())
case = 1
for i in range(0,datacount):
	xBoardH = [0,0,0,0]
	xBoardV = [0,0,0,0]
	xBoardS1 = 0
	xBoardS2 = 0
	yBoardH = [0,0,0,0]
	yBoardV = [0,0,0,0]
	yBoardS1 = 0
	yBoardS2 = 0
	empty = 0

	loadboard(file)
	
#	print xBoardH
#	print xBoardV
#	print yBoardH
#	print yBoardV
#	print xBoardS1
#	print xBoardS2
#	print yBoardS1
#	print yBoardS2
#	print empty

	file.readline()

	maybeDraw = 1
	for i in range(0,4):
			
		if xBoardH[i] == 15:
			print "Case #%d: X won" % case
			maybeDraw = 0
			break

		if yBoardH[i] == 15:
			print "Case #%d: O won" % case
			maybeDraw = 0
			break

		if xBoardH[i] == 15:
			print "Case #%d: X won" % case
			maybeDraw = 0
			break

		if yBoardV[i] == 15:
			print "Case #%d: O won" % case
			maybeDraw = 0
			break

		if xBoardS1 == 15 or xBoardS2 == 15:
			print "Case #%d: X won" % case
			maybeDraw = 0
			break

		if yBoardS1 == 15 or yBoardS2 == 15:
			print "Case #%d: O won" % case
			maybeDraw = 0
			break

	if maybeDraw == 1:
		if empty == 0:
			print "Case #%d: Draw" % case
		else:
			print "Case #%d: Game has not completed" % case

	case += 1
