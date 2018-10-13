import sys

DIMENSION = 4

line = sys.stdin.readline()
NUMBER = int(line.strip())

for case in range(0, NUMBER):
    horizontal = [0] * DIMENSION
    vertical = [0] * DIMENSION
    diagnoal = [0] * 2
    empty = 0
    for row in range(0, DIMENSION):
	line = sys.stdin.readline().strip()
        for column in range(0, DIMENSION):
	    if line[column] == 'X':
                horizontal[row] += 2
                vertical[column] += 2
		if column == row:
                    diagnoal[0] += 2
                elif (column + row + 1) == DIMENSION:
		    diagnoal[1] += 2
	    elif line[column] == 'O':
                horizontal[row] -= 2
                vertical[column] -= 2
		if column == row:
                    diagnoal[0] -= 2
                elif (column + row + 1) == DIMENSION:
		    diagnoal[1] -= 2
	    elif line[column] == 'T':
                horizontal[row] += 1
                vertical[column] += 1
		if column == row:
                    diagnoal[0] += 1
                elif (column + row + 1) == DIMENSION:
		    diagnoal[1] += 1
	    elif line[column] == '.':
                empty += 1
    ## print horizontal, vertical, diagnoal, empty
    output = 'Game has not completed'
    if empty == 0:
        output = 'Draw'
    if ((7 in horizontal) or (8 in horizontal)
        or (7 in vertical) or (8 in vertical)
        or (7 in diagnoal) or (8 in diagnoal)):
        output = 'X won'
    if ((-5 in horizontal) or (-8 in horizontal)
        or (-5 in vertical) or (-8 in vertical)
        or (-5 in diagnoal) or (-8 in diagnoal)):
        output = 'O won'
    print 'Case #%d: %s' % (case + 1, output)
    sys.stdin.readline()
