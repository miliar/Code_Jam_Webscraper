in_file = open( 'input.txt' )
out_file = open( 'output.txt', 'w' )
input_lines = in_file.readlines( )

in_line_index = 0
num_in_cases = int( input_lines[in_line_index] )

in_line_index += 1 ;

in_cases = []

for i in range( num_in_cases ) :
	in_case = []
	for i in range( 4 ) :
		in_case.append( input_lines[in_line_index][0:4] )
		in_line_index += 1 ;
	in_line_index += 1 ;
	in_cases.append( in_case )


def hasFullLine( case, symbol ) :
	won = False
	for line in case :
		full = True
		for square in line :
			if square != symbol and square != 'T' :
				full = False
				break
		if full :
			won = True
			break
	return won

def hasFullColumn( case, symbol ) :
	transposed = zip( *case )
	return hasFullLine( transposed, symbol )

def hasPrimaryDiagonal( case, symbol ) :
	diag = True
	for i in range( 4 ) :
		square = case[i][i]
		if square != symbol and square != 'T' :
			diag = False
			break
	return diag

def hasSecondaryDiagonal( case, symbol ) :
	mirrored = list( case )
	mirrored.reverse( )
	return hasPrimaryDiagonal( mirrored, symbol )

def hasDiagonal( case, symbol ) :
	return hasPrimaryDiagonal( case, symbol ) or hasSecondaryDiagonal( case, symbol )

def hasWon( case, symbol ) :
	return hasFullLine( case, symbol ) or hasFullColumn( case, symbol ) or hasDiagonal( case, symbol )

def hasFinished( case ) :
	for line in case :
		for square in line :
			if square == '.' :
				return False
	return True



def calcState( case ) :
	if hasWon( case, 'X' ) :
		return 'X won'
	elif hasWon( case, 'O' ) :
		return 'O won'
	elif hasFinished( case ) :
		return 'Draw'
	else :
		return 'Game has not completed'
	pass


for i in range( len( in_cases ) ) :
	case = in_cases[i]
	state = calcState( case )
	print >>out_file, 'Case #' + str(i+1) + ': ' + state

