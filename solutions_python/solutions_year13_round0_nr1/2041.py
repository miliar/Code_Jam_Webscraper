# Google Code Jam 2013 - Qualification Round
_input_file = "A-large.in"
_output_file = "A-large.out"
_output_file_object = None

_linesPerCase = 5

def isWin(row):
	global _output_file_object
	sline = set(row)
	if "." not in row:
		if "X" in row and "O" not in row:
			_output_file_object.write("X won\n");
			return True
		elif "O" in row and "X" not in row:
			_output_file_object.write("O won\n");
			return True
	return False
			
with open(_input_file) as fin, open(_output_file , "w") as _output_file_object:
	lines = fin.read().splitlines()
	numOfCases = int(lines[0])
	for x in range(0,numOfCases):
		_output_file_object.write("Case #{0}: ".format(x+1))
		i=1 + x*_linesPerCase
		case = lines[i]+ lines[i+1] + lines[i+2] + lines[i+3]
		row1 = lines[i]
		row2 = lines[i+1]
		row3 = lines[i+2]
		row4 = lines[i+3]
		col1 = lines[i][0] + lines[i+1][0] + lines[i+2][0] + lines[i+3][0]		
		col2 = lines[i][1] + lines[i+1][1] + lines[i+2][1] + lines[i+3][1]		
		col3 = lines[i][2] + lines[i+1][2] + lines[i+2][2] + lines[i+3][2]		
		col4 = lines[i][3] + lines[i+1][3] + lines[i+2][3] + lines[i+3][3]		
		diag1 = lines[i][0] + lines[i+1][1] + lines[i+2][2] + lines[i+3][3]
		diag2 = lines[i][3] + lines[i+1][2] + lines[i+2][1] + lines[i+3][0]
		if not (isWin(row1) or isWin(row2) or isWin(row3) or isWin(row4) or isWin(col1) or isWin(col2) or isWin(col3) or isWin(col4) or isWin(diag1) or isWin(diag2)):
			if "." in case:
				_output_file_object.write("Game has not completed\n")
			else:
				_output_file_object.write("Draw\n")
			
