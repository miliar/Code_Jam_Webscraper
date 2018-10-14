def check(line):
	count_x = 0
	count_o = 0
	t = 0
	if line.find('.') > -1:
		return -1

	for ch in line:
		if ch == 'X':
			count_x = count_x + 1
		elif ch == 'O':
			count_o = count_o + 1
		elif ch == 'T':
			t = 1

	if count_x == 4 or (count_x + t) == 4 :
		return 'X'
	elif count_o == 4 or (count_o + t) == 4:
		return 'O'
	
	return -1
	
#-----------------------------------------------------------
t = int(raw_input())
for i in range(t):
	lines = []
	for j in range(4):
		lines.append(raw_input())

	if i < t-1:
		raw_input()

	dot = False
	draw = True
	for j in range(5):
		row = ""
		column = ""
		if j < 4:
			row = lines[j]
			for line in lines:
				column = column + line[j]
		else:
			for index in range(4):
				row = row + lines[index][index]
				column = column + lines[index][3-index]

		dot = dot or (row.find('.') > -1) or (column.find('.') > -1)

		if check(row) != -1:
			draw = False
			print "Case #" + str(i+1) + ": " + check(row) + " won"
			break

		elif check(column) != -1:
			draw = False
			print "Case #" + str(i+1) + ": " + check(column) + " won"
			break

	if draw:
		if dot:
			print "Case #" + str(i+1) + ": " + "Game has not completed"
		else:
			print "Case #" + str(i+1) + ": " + "Draw"