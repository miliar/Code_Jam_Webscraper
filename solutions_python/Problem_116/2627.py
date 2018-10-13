import sys

numberOfCases = 0
# Board State Constants
X_WON = 'X won'
O_WON = 'O won'
DRAW = 'Draw'
INCOMPLETE = 'Game has not completed'

# Set up the initial board
def createBoard(lines):
	boardState = list()
	for i in xrange(4):
		boardState.append([])
		for j in xrange(4):
			boardState[i].append(lines[i][j])
	return boardState

def checkFourEntries(entries):
	if '.' in entries:
		return INCOMPLETE
	number_x = 0
	number_o = 0
	number_t = 0
	for entry in entries:
		if entry == 'X':
			number_x += 1
		elif entry == 'O':
			number_o += 1
		elif entry == 'T':
			number_t += 1
	if number_x == 4 or (number_x == 3 and number_t == 1):
		return X_WON
	if number_o == 4 or (number_o == 3 and number_t == 1):
		return O_WON

	# Inconclusive for the row
	return None

def handleGameState(line1, line2, line3, line4):
	lines = [line1, line2, line3, line4]
	boardState = createBoard(lines)
	# Check the board states
	possibly_incomplete = False

	# Check horizontals
	for i in xrange(4):
		entries = list()
		for j in xrange(4):
			entries.append(boardState[i][j])
		result = checkFourEntries(entries)
		if result == X_WON or result == O_WON:
			return result
		if result == INCOMPLETE:
			# Track if we have a possibly incomplete board
			possibly_incomplete = True

	# Check verticals
	for i in xrange(4):
                entries = list()
                for j in xrange(4):
                        entries.append(boardState[j][i])
                result = checkFourEntries(entries)
                if result == X_WON or result == O_WON:
                        return result
                if result == INCOMPLETE:
                        # Track if we have a possibly incomplete board
                        possibly_incomplete = True

	# Check the crosses
	entries = list([boardState[0][0], boardState[1][1], boardState[2][2], boardState[3][3]])
	result = checkFourEntries(entries)
        if result == X_WON or result == O_WON:
	        return result
        if result == INCOMPLETE:
                # Track if we have a possibly incomplete board
                possibly_incomplete = True

	entries = list([boardState[0][3], boardState[1][2], boardState[2][1], boardState[3][0]])
        result = checkFourEntries(entries)
        if result == X_WON or result == O_WON:
                return result
        if result == INCOMPLETE:
                # Track if we have a possibly incomplete board
                possibly_incomplete = True

	if possibly_incomplete:
		return INCOMPLETE

	# Must be a draw, no winning lines and not incomplete
	return DRAW

def parseFile(iFile, oFile):
	case = 0
	with open(iFile, 'r') as data:
		with open(oFile, 'w') as results:
			number_of_inputs = int(data.readline())
			for line in data:
				# Now parse the board states 4 lines at a time
				line1 = line
				line2 = data.next()
				line3 = data.next()
				line4 = data.next()

				# Advance past the space
				data.next()
				case += 1
				gameState = handleGameState(line1, line2, line3, line4)
				results.write("Case #" + str(case) + ": " + gameState + '\n')
				
def main():
	# Check arguments
	if len(sys.argv) != 3: 
		sys.exit(1)

	inputFile = sys.argv[1]
	outputFile = sys.argv[2]

	parseFile(inputFile, outputFile)

if __name__ == "__main__":
    main()
