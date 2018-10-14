# T4 parser and evaluator

def ParseInput(f):
	amt = int(f.readline())
	cases = []
	for i in range(1,amt+1):
		box = []
		for j in range(1,5):
			box.append(list(f.readline().strip('\n')))
		f.readline() # Skip the space
		cases.append(box)
	return cases

def transposed(lists):
	if not lists: return []
	return map(lambda *row: list(row), *lists)

def diagonals(case):
	lines = []
	# First diagonal
	line1 = []
	index = 0
	for line in case:
		line1.append(line[index])
		index += 1

	# Second diagonal
	line2 = []
	index = 3
	for line in case:
		line2.append(line[index])
		index -= 1

	lines.append(line1)
	lines.append(line2)
	return lines

def CheckX(case):
	for line in case:
		if '.' not in line and 'O' not in line:
			return True

def CheckO(case):
	for line in case:
		if '.' not in line and 'X' not in line:
			return True

def CheckBlackout(case):
	for line in case:
		if '.' in line:
			return False
	return True

if __name__ == '__main__':
	path = raw_input("File: ")
	cases = None
	with open(path, 'r') as infile:
		cases = ParseInput(infile)

	with open("./outfile", 'w') as outfile:
		casenum = 1
		for case in cases:
			horizontal = case
			vertical = transposed(case)
			diagonal = diagonals(case)

			if CheckX(horizontal) or CheckX(vertical) or CheckX(diagonal):
				outfile.write("Case #%r: X won\n" % casenum)
			elif CheckO(horizontal) or CheckO(vertical) or CheckO(diagonal):
				outfile.write("Case #%r: O won\n" % casenum)
			elif CheckBlackout(case):
				outfile.write("Case #%r: Draw\n" % casenum)
			else:
				outfile.write("Case #%r: Game has not completed\n" % casenum)
			casenum += 1