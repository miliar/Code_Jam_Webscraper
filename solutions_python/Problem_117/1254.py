def eval(matrice, line, col) :
	for x in xrange(line) :
		for y in xrange(col) :
			temp = matrice[x][y]
			tempx = x
			line_chek = True
			col_chek = True
			while tempx >= 0 :
				if matrice[tempx][y] > temp :
					line_chek = False
				tempx -= 1
			tempx = x
			while tempx < line :
				if matrice[tempx][y] > temp :
					line_chek = False
				tempx += 1
			tempy = y
			while tempy >= 0 :
				if matrice[x][tempy] > temp :
					col_chek = False
				tempy -= 1
			tempy = y
			while tempy < col :
				if matrice[x][tempy] > temp :
					col_chek = False
				tempy += 1
			if not line_chek and not col_chek :
				return False
	return True
	
f = open('B-large.in', 'r')
input = f.read()
input_len = len(input)
f.close()
out = open('output_lawnmower.txt', 'w')

offset = 0
nbtest = ''
while input[offset] != '\n' :
	nbtest += input[offset]
	offset += 1
nbtest = int(nbtest)
offset += 1
for nb in xrange(nbtest) :
	line = ''
	col = ''
	while input[offset] != ' ' :
		line += input[offset]
		offset += 1
	line = int(line)
	offset += 1
	while input[offset] != '\n' :	
		col += input[offset]
		offset += 1
	col = int(col)
	offset += 1
	
	currentline = 0
	matrice = []
	while currentline < line :
		currentcol = 0
		matrice_temp = []
		while currentcol < col :
			temp = ''
			while offset < input_len and input[offset] != '\n' and input[offset] != ' ' :
				temp += input[offset]
				offset += 1
			currentcol += 1
			matrice_temp.append(int(temp))
			offset += 1
		matrice.append(matrice_temp)
		currentline += 1

	print(line),
	print(col)
	for x in xrange(line) :
		for y in xrange(col) :
			print(matrice[x][y]),
		print (' ')
		
	if eval(matrice, line, col) :
		print('Case #' + str(nb + 1) + ': YES')
		out.write('Case #' + str(nb + 1) + ': YES\n')
	else :
		print('Case #' + str(nb + 1) + ': NO')
		out.write('Case #' + str(nb + 1) + ': NO\n')
out.close()