def riacho(nome,i,j):
	input = matrix[i][j]
	matrix[i][j] = nome
	if input == "N":
		riacho(nome,i-1,j)
	if input == "S":
		riacho(nome,i+1,j)
	if input == "W":
		riacho(nome,i,j-1)
	if input == "E":
		riacho(nome,i,j+1)
	if i>0 and matrix[i-1][j] == "S":
		riacho(nome,i-1,j)
	if j>0 and matrix[i][j-1] == "E":
		riacho(nome,i,j-1)
	if i+1<h and matrix[i+1][j] == "N":
		riacho(nome,i+1,j)
	if j+1<w and matrix[i][j+1] == "W":
		riacho(nome,i,j+1)

def fill(index):
	c_i = c_j = -1 
	for i in xrange(h):
		for j in xrange(w):
			if not (matrix[i][j] in letras):
				c_i = i
				c_j = j
				break
		if c_i != -1:
			break
	if c_i != -1:
		riacho(letras[index],c_i,c_j)
		return True 
	else:
		return False 

letras = "abcdefghijklmnopqrstuvwxyz"
cases = int(raw_input())

for i in xrange(cases):
	r = raw_input().split()
	h = int(r[0])
	w = int(r[1])
	matrix = [None for j in xrange(h)]
	matrix2 = [[None for k in xrange(w)] for j in xrange(h)]

	for j in xrange(h):
		matrix[j] = raw_input().split()

	for j in xrange(h):
		for k in xrange(w):
			dir = "K"
			lower = int(matrix[j][k])
			if j>0 and lower > int(matrix[j-1][k]):
				lower = int(matrix[j-1][k])
				dir = "N"
			if k>0 and lower > int(matrix[j][k-1]):
				lower = int(matrix[j][k-1])
				dir = "W"
			if k+1<w and lower > int(matrix[j][k+1]):
				lower = int(matrix[j][k+1])
				dir = "E"
			if j+1<h and lower > int(matrix[j+1][k]):
				lower = int(matrix[j+1][k])
				dir = "S"
			matrix2[j][k] = dir

	matrix = matrix2
	toFill = True
	n = 0
	while toFill:
		toFill = fill(n)
		n+=1
	print "Case #"+str(i+1)+":"
	
	for j in xrange(h):
		string = ""
		for k in xrange(w):
			string += matrix[j][k]+" "

		print string.strip()
#preencher com a's e b's



