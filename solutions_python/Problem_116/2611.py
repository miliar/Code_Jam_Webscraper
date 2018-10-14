

strs = 'Case #'
n = 0
f = open('A-large.in', 'r')
fw = open('A.out', 'w')
line = f.readline()
while line != '':
	n += 1
	isEmpty = False
	rowX = [0 for i in range(4)]
	colX = [0 for i in range(4)]
	diagX =  [0 for i in range(2)]
	rowO = [0 for i in range(4)]
	colO = [0 for i in range(4)]
	diagO =  [0 for i in range(2)]
	for i in range(4):
		line = f.readline()
		print line
		for j in range(4):
			if line[j] == 'X':
				rowX[i] += 1
				colX[j] += 1
				if i == j:
					diagX[0] += 1
				elif i+j == 3:
					diagX[1] += 1
			if line[j] == 'O':
				rowO[i] += 1
				colO[j] += 1
				if i == j:
					diagO[0] += 1
				elif i+j == 3:
					diagO[1] += 1
			if line[j] == 'T':
				rowX[i] += 1
				colX[j] += 1
				if i == j:
					diagX[0] += 1
				elif i+j == 3:
					diagX[1] += 1
					
				rowO[i] += 1
				colO[j] += 1
				if i == j:
					diagO[0] += 1
				elif i+j == 3:
					diagO[1] += 1
			if line[j] == '.':
				isEmpty = True
		
	if (4 in rowX) or (4 in colX) or (4 in diagX):
		fw.write(strs+str(n)+': X won\n')
	elif (4 in rowO) or (4 in colO) or (4 in diagO):
		fw.write(strs+str(n)+': O won\n')
	elif isEmpty:
		fw.write(strs+str(n)+': Game has not completed\n')
	else:
		fw.write(strs+str(n)+': Draw\n')
	line = f.readline()
