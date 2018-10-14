from sys import *

def test():
	win_x, win_o = 0, 0
	dot = False
	
	# Read
	rows = []
	for row_i in range(4):
		row = stdin.readline()
		if len(row) != 5:
			row = stdin.readline()
		rows.append(row)

	# Check row
	for row in rows:
		x, o = 0, 0
		for cur in range(4):
			if row[cur] == 'X':
				x += 1
			elif row[cur] == 'O':
				o += 1
			elif row[cur] == 'T':
				x += 1
				o += 1
			else:
				dot = True
		win_x += int(x / 4)
		win_o += int(o / 4)

	# Check column
	for cur in range(4):
		x, o = 0, 0
		for row in rows:
			if row[cur] == 'X':
				x += 1
			elif row[cur] == 'O':
				o += 1
			elif row[cur] == 'T':
				x += 1
				o += 1
		win_x += int(x / 4)
		win_o += int(o / 4)

	# Check \
	x, o = 0, 0
	for cur in range(4):
		if rows[cur][cur] == 'X':
			x += 1
		elif rows[cur][cur] == 'O':
			o += 1
		elif rows[cur][cur] == 'T':
			x += 1
			o += 1
	win_x += int(x / 4)
	win_o += int(o / 4)

	# Check /
	x, o = 0, 0
	for cur in range(4):
		if rows[cur][-cur - 2] == 'X':
			x += 1
		elif rows[cur][-cur - 2] == 'O':
			o += 1
		elif rows[cur][-cur - 2] == 'T':
			x += 1
			o += 1
	win_x += int(x / 4)
	win_o += int(o / 4)
	
	return (win_x, win_o, dot)

T = int(stdin.readline())
for t in range(T):
	x, o, dot = test()
	if dot and x == 0 and o == 0:
		print('Case #', t + 1, ': Game has not completed', sep='')
	elif x > 0:
		print('Case #', t + 1, ': X won', sep='')
	elif o > 0:
		print('Case #', t + 1, ': O won', sep='')
	else:
		print('Case #', t + 1, ': Draw', sep='')
