__author__ = 'thomas@thomas-maier.net'

import codejamhelper as h

def main():
	lines = h.get_input()
	cases = h.get_case_tuples(lines, (str, str, str, str, str))
	cases = map(lambda x: list(x)[:-1], cases)

	solutions = []
	for case in cases:
		if find_line(case, ['X', 'T']):
			solutions.append('X won')
			continue
		if find_line(case, ['O', 'T']):
			solutions.append('O won')
			continue
		if find_dots(case):
			solutions.append('Game has not completed')
			continue
		solutions.append('Draw')

	h.save_output(solutions)


def find_line(case, symbols):

	#horizontal
	for row in case:
		if check_match(row, symbols): return True

	#vertical
	for n in xrange(len(case[0])):
		col = []
		for row in case:
			col.append(row[n])
		if check_match(col, symbols): return True

	#diagonal
	diag1 = []; diag2 = []
	for i in xrange(len(case)):
		j = len(case) - i - 1
		diag1.append(case[i][i])
		diag2.append(case[j][i])
	if check_match(diag1, symbols): return True
	if check_match(diag2, symbols): return True

	return False


def check_match(list, symbols):
	for elem in list:
		if elem not in symbols:
			return False
	return True

def find_dots(case):
	for row in case:
		for elem in row:
			if elem == '.': return True
	return False

if __name__ == "__main__":
	main()