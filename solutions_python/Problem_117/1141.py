
def line2intlist(line):
    list = line.split()
    numbers = [ int(x) for x in list ]
    return numbers
	
def processLawn(lawnSize, lawn):
	rowCount = lawnSize[0]
	colCount = lawnSize[1]
	
	lawnCellVisiblity = []
	for y in xrange(0, rowCount):
		lawnCellVisiblity.append([])
		for x in xrange(0, colCount):
			lawnCellVisiblity[y].append([0, 0])
	
	#for y in xrange(0, rowCount):
	#	print lawnCellVisiblity[y]
	
	# Scan from left to right
	for y in xrange(0, rowCount):
		minVisibleHeight = 0 # Every cell with height >= minVisibleHeight = visible
		for x in xrange(0, colCount):
			currentHeight = lawn[y][x]
			if currentHeight >= minVisibleHeight:
				lawnCellVisiblity[y][x][0] += 1
				minVisibleHeight = currentHeight;
	
	#for y in xrange(0, rowCount):
	#	print lawnCellVisiblity[y]
	
	# Scan from right to left
	for y in xrange(0, rowCount):
		minVisibleHeight = 0 # Every cell with height >= minVisibleHeight = visible
		for x in reversed(xrange(0, colCount)):
			currentHeight = lawn[y][x]
			if currentHeight >= minVisibleHeight:
				lawnCellVisiblity[y][x][0] += 1
				minVisibleHeight = currentHeight;
				
				
	# Scan from up to down
	for x in xrange(0, colCount):
		minVisibleHeight = 0 # Every cell with height >= minVisibleHeight = visible
		for y in xrange(0, rowCount):
			currentHeight = lawn[y][x]
			if currentHeight >= minVisibleHeight:
				lawnCellVisiblity[y][x][1] += 1
				minVisibleHeight = currentHeight;
	
	# Scan from down to up
	for x in xrange(0, colCount):
		minVisibleHeight = 0 # Every cell with height >= minVisibleHeight = visible
		for y in reversed(xrange(0, rowCount)):
			currentHeight = lawn[y][x]
			if currentHeight >= minVisibleHeight:
				lawnCellVisiblity[y][x][1] += 1
				minVisibleHeight = currentHeight;
	
	everyCellIsVisible = True
	for y in xrange(0, rowCount):
		if not everyCellIsVisible: break
		for x in xrange(0, colCount):
			if not (lawnCellVisiblity[y][x][0] == 2 or lawnCellVisiblity[y][x][1] == 2):
				everyCellIsVisible = False
				break
	
	return "YES" if everyCellIsVisible else "NO"

testcases = input()

for caseNum in xrange(0, testcases):
	lawn = []
	
	lawnSize = line2intlist(raw_input())
	rowCount = lawnSize[0]
	
	for r in xrange(0, rowCount):
		lawn.append(line2intlist(raw_input()))
		
	# print lawn
	
	# Expect empty line
	#raw_input()
	possible = processLawn(lawnSize, lawn)
	print("Case #%i: %s" % (caseNum + 1, possible))
