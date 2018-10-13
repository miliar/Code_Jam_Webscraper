import sys

def main():
	cases = int( sys.stdin.readline().strip() )

	for c in range(0,cases):
		tmp = []
		for line in range(0,4):
			tmp.append( list(sys.stdin.readline().strip()) )
		# The empty row
		sys.stdin.readline()

		print( "Case #%s: %s" % (c+1,check(tmp)) )

def check(x):
	# Chack diagonals
	if ( ( x[0][0] == 'X' or x[0][0] == 'T' ) and
		( x[1][1] == 'X' or x[1][1] == 'T' ) and
		( x[2][2] == 'X' or x[2][2] == 'T' ) and
		( x[3][3] == 'X' or x[3][3] == 'T' ) ):
		return "X won"
	if ( ( x[0][3] == 'X' or x[0][3] == 'T' ) and
		( x[1][2] == 'X' or x[1][2] == 'T' ) and
		( x[2][1] == 'X' or x[2][1] == 'T' ) and
		( x[3][0] == 'X' or x[3][0] == 'T' ) ):
		return "X won"

	if ( ( x[0][0] == 'O' or x[0][0] == 'T' ) and
		( x[1][1] == 'O' or x[1][1] == 'T' ) and
		( x[2][2] == 'O' or x[2][2] == 'T' ) and
		( x[3][3] == 'O' or x[3][3] == 'T' ) ):
		return "O won"
	if ( ( x[0][3] == 'O' or x[0][3] == 'T' ) and
		( x[1][2] == 'O' or x[1][2] == 'T' ) and
		( x[2][1] == 'O' or x[2][1] == 'T' ) and
		( x[3][0] == 'O' or x[3][0] == 'T' ) ):
		return "O won"

	# Check rows and columns
	tmp = True
	for i in range(0,4):
		if ( ( x[i][0] == 'X' or x[i][0] == 'T' ) and
			( x[i][1] == 'X' or x[i][1] == 'T' ) and
			( x[i][2] == 'X' or x[i][2] == 'T' ) and
			( x[i][3] == 'X' or x[i][3] == 'T' ) ):
			return "X won"
		if ( ( x[0][i] == 'X' or x[0][i] == 'T' ) and
			( x[1][i] == 'X' or x[1][i] == 'T' ) and
			( x[2][i] == 'X' or x[2][i] == 'T' ) and
			( x[3][i] == 'X' or x[3][i] == 'T' ) ):
			return "X won"

		if ( ( x[i][0] == 'O' or x[i][0] == 'T' ) and
			( x[i][1] == 'O' or x[i][1] == 'T' ) and
			( x[i][2] == 'O' or x[i][2] == 'T' ) and
			( x[i][3] == 'O' or x[i][3] == 'T' ) ):
			return "O won"
		if ( ( x[0][i] == 'O' or x[0][i] == 'T' ) and
			( x[1][i] == 'O' or x[1][i] == 'T' ) and
			( x[2][i] == 'O' or x[2][i] == 'T' ) and
			( x[3][i] == 'O' or x[3][i] == 'T' ) ):
			return "O won"	

		# Check draws
		for j in range(0,4):
			if x[i][j] == '.':
				tmp = False

	if tmp:
		return "Draw"

	return "Game has not completed"

if __name__ == '__main__':
	main()