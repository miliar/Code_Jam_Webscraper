import sys

def main(filename):
	result = ''
	file = open(filename)
	numberOfTests = int(file.readline())
	for i in range(numberOfTests):
		lines = []
		for j in range(4):
			lines.append(file.readline().strip())
		result += 'Case #%d: %s\n' % (i+1,solveTicTacToe(lines))
		file.readline()
	file.close()
	return result
	
def solveTicTacToe(lines):
	result = checkLines(lines)
	if result is not None:
		return result
	result = checkColumns(lines)
	if result is not None:
		return result
	result = checkDiagonal(lines)
	if result is not None:
		return result
	if ''.join(lines).count('.') == 0:
		return 'Draw'
	else:
		return 'Game has not completed'
		
def checkLines(lines):
	for line in lines:
		result = checkLine(line)
		if result is not None:
			return result

def checkLine(line):
	x = line.count('X') + line.count('T')
	o = line.count('O') + line.count('T')
	if x == 4:
		return 'X won'
	if o == 4:
		return 'O won'
			
def checkColumns(lines):
	for columnIndex in range(len(lines)):
		column = ''
		for line in lines:
			column += line[columnIndex]
		result = checkLine(column)
		if result is not None:
			return result

def checkDiagonal(lines):
	line1 = ''
	for index in range(len(lines)):
		line1 += lines[index][index]
	result = checkLine(line1)
	if result is not None:
		return result
	line2 = ''
	for index in range(len(lines)):
		line2 += lines[index][len(lines)-1-index]
	result = checkLine(line2)
	if result is not None:
		return result
	
if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'Not enough files specified'
		sys.exit(1)
	inputfilename = sys.argv[1]
	outputfilename = sys.argv[2]
	result = main(inputfilename)
	outputfile = open(outputfilename, 'w')
	outputfile.write(result)
	outputfile.close()
	print result