
def count(arr,startX,startY,deltaX,deltaY):
	
	TCount = 0
	XCount = 0
	OCount = 0
	EmptyCount = 0

	for i in xrange(4):
		currentX = startX + i*deltaX
		currentY = startY + i*deltaY

		currentSpace = arr[currentY][currentX]

		if currentSpace == '.':
			EmptyCount+=1
		elif currentSpace == "T":
			TCount += 1
		elif currentSpace == "O":
			OCount += 1
		elif currentSpace == "X":
			XCount += 1


	return (TCount,XCount,OCount,EmptyCount)





def processArray(arr):

	emptySpacesLeft = False

	for row in xrange(4):
		TCount,XCount,OCount,EmptyCount = count(arr,0,row,1,0)
		if EmptyCount != 0:
			emptySpacesLeft = True
		elif XCount + TCount == 4:
			return "X won"
		elif OCount + TCount == 4:
			return "O won"

	for column in xrange(4):
		TCount,XCount,OCount,EmptyCount = count(arr,column,0,0,1)
		if EmptyCount != 0:
			emptySpacesLeft = True
		elif XCount + TCount == 4:
			return "X won"
		elif OCount + TCount == 4:
			return "O won"

	TCount,XCount,OCount,EmptyCount = count(arr,0,0,1,1)
	if EmptyCount != 0:
		emptySpacesLeft = True
	elif XCount + TCount == 4:
		return "X won"
	elif OCount + TCount == 4:
		return "O won"

	TCount,XCount,OCount,EmptyCount = count(arr,0,3,1,-1)
	if EmptyCount != 0:
		emptySpacesLeft = True
	elif XCount + TCount == 4:
		return "X won"
	elif OCount + TCount == 4:
		return "O won"


	if emptySpacesLeft:
		return "Game has not completed"
	else:
		return "Draw"

			



with open('input','r') as fileIn:
	with open('output','w') as fileOut:

		cases = int(fileIn.readline())
		print cases

		for i in xrange(cases):
			arr = [ [] for _ in xrange(4)]

			for y in xrange(4):
				line = fileIn.readline()
				for x in xrange(4):
					arr[y].append(line[x])

			#print arr

			result = "Case #%d: " % (i+1) + processArray(arr)
			print result

			fileOut.write(result + '\n')





			fileIn.readline()

