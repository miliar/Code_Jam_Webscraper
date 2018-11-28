import collections

#f = open('./ex.txt', 'r')
f = open('./A-large.in', 'r')
f_results = open('./result.txt', 'w')

cases = int(f.readline())

for case in range(cases):
#	print ""
#	print "Case " + str(case + 1)

	b = []
	for t in range(4):
		b += list(f.readline())
	f.readline()

#	print b
	
	res = collections.deque()
	res.append(b[0:4])
	res.append(b[5:9])
	res.append(b[10:14])
	res.append(b[15:19])
	res.append([b[0], b[5], b[10], b[15]])
	res.append([b[1], b[6], b[11], b[16]])
	res.append([b[2], b[7], b[12], b[17]])
	res.append([b[3], b[8], b[13], b[18]])
	res.append([b[0], b[6], b[12], b[18]])
	res.append([b[3], b[7], b[11], b[15]])
#	print res
	
	not_found = True
	cntX = 0
	cntO = 0
	draw = True

	while not_found and len(res) > 0:
#		print "res"
		cntX = 0
		cntO = 0
		l = res.popleft()
		for sign in l:
			if sign == 'X':
				cntX += 1
			elif sign == 'O':
				cntO += 1
			elif sign == 'T':
				cntX += 1
				cntO += 1
			else:
				draw = False
		if cntX == 4 or cntO == 4:
			not_found = False

	if cntX == 4:
		results = "X won"
	elif cntO == 4:
		results = "O won"
	elif draw:
		results = "Draw"
	else:
		results = "Game has not completed"
        f_results.write("Case #" + str(case + 1) + ": " + results + "\n")

			
		


		
