import sys

f = open(sys.argv[1], 'r')
line = f.readline().split(' ')
cases = int(line[0])

for case in range(cases):
	case = case + 1

	lines = []
	lines.append(f.readline())
	lines.append(f.readline())
	lines.append(f.readline())
	lines.append(f.readline())
	f.readline()

	Xwon = False
	Owon = False
	dot = False

	for line in range(4):
		countX = {}
		countX['X'] = 0
		countX['O'] = 0
		countX['T'] = 0
		countX['.'] = 0

		countY = {}
		countY['X'] = 0
		countY['O'] = 0
		countY['T'] = 0
		countY['.'] = 0

		for char in range(4):
			countX[lines[line][char]] += 1
			countY[lines[char][line]] += 1

		if countX['X'] == 4:
			Xwon = True

		if countX['O'] == 4:
			Owon = True

		if countX['T'] == 1:
			if countX['X'] == 3:
				Xwon = True

			if countX['O'] == 3:
				Owon = True

		if countY['X'] == 4:
			Xwon = True

		if countY['O'] == 4:
			Owon = True

		if countY['T'] == 1:
			if countY['X'] == 3:
				Xwon = True

			if countY['O'] == 3:
				Owon = True

		if countX['.'] > 0 or countY['.'] > 0:
			dot = True

	countD1 = {}
	countD1['X'] = 0
	countD1['O'] = 0
	countD1['T'] = 0
	countD1['.'] = 0

	countD2 = {}
	countD2['X'] = 0
	countD2['O'] = 0
	countD2['T'] = 0
	countD2['.'] = 0

	for char in range(4):
		countD1[lines[char][char]] += 1
		countD2[lines[char][3 - char]] += 1

	if countD1['X'] == 4:
		Xwon = True

	if countD1['O'] == 4:
		Owon = True

	if countD1['T'] == 1:
		if countD1['X'] == 3:
			Xwon = True

		if countD1['O'] == 3:
			Owon = True

	if countD2['X'] == 4:
		Xwon = True

	if countD2['O'] == 4:
		Owon = True

	if countD2['T'] == 1:
		if countD2['X'] == 3:
			Xwon = True

		if countD2['O'] == 3:
			Owon = True

	reason = ""

	if Xwon:
		reason = "X won"

	elif Owon:
		reason = "O won"

	elif not dot:
		reason = "Draw"

	else:
		reason = "Game has not completed"

	print "Case #%i: %s" % (case, reason)