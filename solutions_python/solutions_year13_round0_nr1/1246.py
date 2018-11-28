import sys
readInts = lambda : map(int, raw_input().strip().split())
readArgs = lambda : raw_input().strip().split()
write = lambda *s: sys.stdout.write(' '.join(map(str, s)))
#exit = lambda status = 0 : sys.exit(status)
isX = lambda ch : ch == 'X' or ch == 'T'
isO = lambda ch : ch == 'O' or ch == 'T'
isEmpty = lambda ch : ch == '.'

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
T = readInts()[0]
for i in range(1, T + 1):
	if i > 1:
		raw_input()
	write('Case #%d: ' % i)
	data = []
	empty = False
	flag = False
	for i in range(4):
		data.append(raw_input().strip())
		for j in range(4):
			if empty:
				break
			if isEmpty(data[i][j]):
				empty = True
				break
	# Row Check
	for i in range(4):
		allX, allO = True, True
		for j in range(4):
			if not isX(data[i][j]):
				allX = False
			if not isO(data[i][j]):
				allO = False
		if allX:
			print 'X won'
			flag = True
			break
		if allO:
			print 'O won'
			flag = True
			break
	if flag:
		continue
	
	# Col Check
	for i in range(4):
		allX, allO = True, True
		for j in range(4):
			if not isX(data[j][i]):
				allX = False
			if not isO(data[j][i]):
				allO = False
		if allX:
			print 'X won'
			flag = True
			break
		if allO:
			print 'O won'
			flag = True
			break
	
	if flag:
		continue
	
	# 0, 0 -> 3, 3 Diag Check
	allX, allO = True, True
	for i in range(4):
		if not isX(data[i][i]):
			allX = False
		if not isO(data[i][i]):
			allO = False
	if allX:
		print 'X won'
		flag = True
		continue
	if allO:
		print 'O won'
		flag = True
		continue
	# 0, 3 -> 3, 0 Diag Check
	allX, allO = True, True
	for i in range(4):
		if not isX(data[i][3 - i]):
			allX = False
		if not isO(data[i][3 - i]):
			allO = False
	
	if allX:
		print 'X won'
		flag = True
		continue
	if allO:
		print 'O won'
		flag = True
		continue

	# Nobody wins
	if empty:
		print 'Game has not completed'
	else:
		print 'Draw'
