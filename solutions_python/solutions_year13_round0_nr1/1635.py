T = input()

def solve(inp):
	xx = ["".join(i) for i in inp]
	xx = "".join(xx)

	for i in range(4):
		for j in range(4):
			if i==3 and j==0:
				x = "".join([inp[i][j], inp[i-1][j+1], inp[i-2][j+2],inp[i-3][j+3]])
				if 'T' in x: 
					x = x.replace('T',"")
					if x == "XXX":
						return 0
					elif x == "OOO": 
						return 1
				else:
					if x == "XXXX":
						return 0
					elif x == "OOOO": 
						return 1

			if j == 0:
					x = "".join([inp[i][j], inp[i][j+1], inp[i][j+2], inp[i][j+3]])
				  	if 'T' in x: 
						x = x.replace('T',"")
				  		if x == "XXX":
							return 0
						elif x == "OOO": 
							return 1
					else:
						if x == "XXXX":
							return 0
						elif x == "OOOO": 
							return 1
			if i == 0:
					x = "".join([inp[i][j], inp[i+1][j], inp[i+2][j], inp[i+3][j]])
				  	if 'T' in x: 
						x = x.replace('T',"")
				  		if x == "XXX":
							return 0
						elif x == "OOO": 
							return 1
					else:
						if x == "XXXX":
							return 0
						elif x == "OOOO": 
							return 1

			if i==0 and j==0:
				x = "".join([inp[i][j], inp[i+1][j+1], inp[i+2][j+2],inp[i+3][j+3]])
				if 'T' in x: 
					x = x.replace('T',"")
					if x == "XXX":
						return 0
					elif x == "OOO": 
						return 1
				else:
					if x == "XXXX":
						return 0
					elif x == "OOOO": 
						return 1

	if '.' in x: return 2				
	return 3




for t in range(T):
	inp = []
	for row in range(4):
		data=raw_input().strip()
		inp.append(list(data))

	if t != T-1: raw_input()
	res = solve(inp)

	if res == 0:   print "Case #%d: X won" % (t+1)
	elif res == 1: print "Case #%d: O won" % (t+1)
	elif res == 2: print "Case #%d: Game has not completed" % (t+1)
	elif res == 3: print "Case #%d: Draw" % (t+1)