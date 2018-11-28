#!/usr/bin/env python
def process_file(file):
	fsock = open(file)
	text = fsock.read()
	fsock.close()
	lines = text.split('\n')
	return lines

def process_lines(lines):
	ans = []
	first = True
	numCases = int(lines[0])
	lineIndex = 1
	for caseIndex in range(numCases):
		case = []
		for row in range(4):
			case.append(list(lines[lineIndex]))
			lineIndex += 1
		ans.append(case)
		lineIndex += 1
	return ans

def process_case(case):
	completed = True
	for i in range(4):
		for j in range(4):
			if completed and case[i][j] == '.':
				completed = False
			winner = checkWinner(case, i, j, 1, 0)
			if winner:
				return winner + ' won'
			winner = checkWinner(case, i, j, 0, 1)
			if winner:
				return winner + ' won'
			winner = checkWinner(case, i, j, 1, 1)
			if winner:
				return winner + ' won'
			winner = checkWinner(case, i, j, 1, -1)
			if winner:
				return winner + ' won'
	if completed:
		return 'Draw'
	else:
		return 'Game has not completed'

def checkWinner(case, i, j, iDir, jDir):
	# Check out of bounds
	if i + (3 * iDir) > 3 or j + (3 * jDir) > 3:
		return None
	player = case[i][j]
	if player == '.':
		return None
	for count in range(1, 4):
		next = case[i + (count * iDir)][j + (count * jDir)]
		if next != player and next != 'T':
			return None
	return player

if __name__ == "__main__":
	import sys
	filename = sys.argv[1]
	lines = process_file(filename)
	cases = process_lines(lines)
	c = 0
	for case in cases:
		c += 1
		print "Case #%d: %s" % (c, process_case(case))