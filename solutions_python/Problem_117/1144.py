from sys import *

def test():
	# Read
	size = stdin.readline().split(' ')
	h, w = int(size[0]), int(size[1])
	rows = []
	ok = []
	for y in range(h):
		row = stdin.readline().split(' ')
		ok_line = []
		for x in range(w):
			row[x] = int(row[x])
			ok_line.append(False)
		rows.append(row)
		ok.append(ok_line)

	# Check row
	for y in range(h):
		max = 1
		for x in range(w):
			if rows[y][x] > max:
				max = rows[y][x]
		for x in range(w):
			if rows[y][x] == max:
				ok[y][x] = True
	
	# Check column
	for x in range(w):
		max = 1
		for y in range(h):
			if rows[y][x] > max:
				max = rows[y][x]
		for y in range(h):
			if rows[y][x] == max:
				ok[y][x] = True

	for y in range(h):
		for x in range(w):
			if not ok[y][x]:
				return False
	return True

T = int(stdin.readline())
for t in range(T):
	if test():
		print('Case #', t + 1, ': YES', sep='')
	else:
		print('Case #', t + 1, ': NO', sep='')