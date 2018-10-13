# reult is -1 as initial value
# result is 0 if 0 wins
# result is 1 if X wins
# result is 2 if draw
# result is 3 if game not over
def getResultForLine (line, emptyCell):
	#print line
	result = -1
	resultFound = False
	for elem in line:
		if elem == '.':
			result = 3
			break
		if result == 2:
			continue
		if elem == 'X':
			if result == 0:
				result = 2 
			elif result == -1:
				result = 1
		elif elem == 'O':
			if result == 1:
				result = 2
			elif result == -1:
				result = 0
	if result in [0,1]:
		resultFound = True
	elif result == 3:
		emptyCell = True

	return (result, resultFound, emptyCell)

T = int(raw_input().strip())
#print T

for i in xrange(T):
	print 'Case #%s:' %(i+1),
	board = []
	emptyCell = False
	for j in xrange(4):
		elements = raw_input().strip()
		board.append(elements)
	resultFound = False
	for row in xrange(4):
		(result, resultFound, emptyCell) = getResultForLine(board[row], emptyCell)
		if resultFound:
			break
		

	if not resultFound:		
		for row in xrange(4):
			line = ''
			for col in xrange(4):
				line = line + board[col][row]
			(result, resultFound, emptyCell) = getResultForLine(line, emptyCell)
			if resultFound:
				break

					
	if not resultFound:
		line = ''
		for row in xrange(4):
			 line = line + board[row][row]
		(result, resultFound, emptyCell) = getResultForLine(line, emptyCell)

	if not resultFound:
		line = ''
		for row in xrange(4):
			line = line + board[row][4-row-1]
		(result, resultFound, emptyCell) = getResultForLine(line, emptyCell)

	if resultFound:
		if result == 0:
			print ' O won'
		elif result == 1:
			print ' X won'
	elif emptyCell:
		print ' Game has not completed'
	else:
		print ' Draw'
			
	raw_input()
