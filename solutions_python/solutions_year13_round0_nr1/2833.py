import sys

def check(elements):
	sum_x = 0
	sum_y = 0
	empty = False
	for e in elements:
		if e == 'X':
			sum_x += 1
		elif e == 'O':
			sum_y += 1
		elif e == 'T':
			sum_x += 1
			sum_y += 1
		elif e == '.':
			empty = True

	return [sum_x, sum_y, empty]


def confirm(elements, w):
	outcome = check(elements)
	ret = [False, outcome[2]]
	if outcome[0] == 4:
		print "X won"
		w.write("X won\n")
		ret[0] = True
	elif outcome[1] == 4:
		print "O won"
		w.write("O won\n")
		ret[0] = True
	return ret

def travel(matrix, w):
	empty = False
	for i in range(4):
		status = confirm(matrix[i], w)
		if status[0]:
			return
		empty = status[1] if not empty else status[1]

	transpose = zip(*matrix)
	for j in range(4):
		status = confirm(transpose[j], w)
		if status[0]:
			return
		empty = status[1] if not empty else status[1]

	# left-right diag
	lrdiag = [matrix[i][i] for i in range(4)]
	status = confirm(lrdiag, w)
	if status[0]:
		return
	empty = status[1] if not empty else status[1]

	# right-left diag
	rldiag = [matrix[i][3-i] for i in range(4)]
	status = confirm(rldiag, w)
	if status[0]:
		return
	empty = status[1] if not empty else status[1]

	# if we're still here then either it's a tie of game's incomplete
	if empty:
		print "Game has not completed"
		w.write("Game has not completed\n")
	else:
		print "Draw"
		w.write("Draw\n")

def get_input():
	f = open('input.in')
	w = open('output.out', 'w')
	cases = int(f.readline())
	matrices = []
	matrix = []
	for line in f.readlines():
		if line == '\n':
			matrices.append(matrix)
			matrix = []
		else:
			matrix.append(list(line.rstrip()))

	f.close()

	for i, v in enumerate(matrices):
		print "Case #%d: " % (i+1),
		w.write("Case #%d: " % (i+1))
		travel(v, w)

if __name__ == '__main__':
	get_input()