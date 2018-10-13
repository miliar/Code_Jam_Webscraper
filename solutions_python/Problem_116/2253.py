f = open("A-large.in", 'r')
g = open("output.out", 'w')
cases = int(f.readline())
i = 0

while i<cases:

 	i = i+1

	matrix = ['.' for x in xrange(4)]
	for y in xrange(4):
		matrix[y] = f.readline().split()[0]
	f.readline()
	
	## X WON
	if (matrix[0][0] == 'X' or matrix[0][0] == 'T') and (matrix[0][1] == 'X' or matrix[0][1] == 'T') and (matrix[0][2] == 'X' or matrix[0][2] == 'T') and (matrix[0][3] == 'X' or matrix[0][3] == 'T'): 
		g.write("Case #" + str(i) + ": X won" + "\n")
	elif (matrix[1][0] == 'X' or matrix[1][0] == 'T') and (matrix[1][1] == 'X' or matrix[1][1] == 'T') and (matrix[1][2] == 'X' or matrix[1][2] == 'T') and (matrix[1][3] == 'X' or matrix[1][3] == 'T'): 
		g.write("Case #" + str(i) + ": X won" + "\n")
	elif (matrix[2][0] == 'X' or matrix[2][0] == 'T') and (matrix[2][1] == 'X' or matrix[2][1] == 'T') and (matrix[2][2] == 'X' or matrix[2][2] == 'T') and (matrix[2][3] == 'X' or matrix[2][3] == 'T'): 
		g.write("Case #" + str(i) + ": X won" + "\n")
	elif (matrix[3][0] == 'X' or matrix[3][0] == 'T') and (matrix[3][1] == 'X' or matrix[3][1] == 'T') and (matrix[3][2] == 'X' or matrix[3][2] == 'T') and (matrix[3][3] == 'X' or matrix[3][3] == 'T'): 
		g.write("Case #" + str(i) + ": X won" + "\n")
	elif (matrix[0][0] == 'X' or matrix[0][0] == 'T') and (matrix[1][0] == 'X' or matrix[1][0] == 'T') and (matrix[2][0] == 'X' or matrix[2][0] == 'T') and (matrix[3][0] == 'X' or matrix[3][0] == 'T'): 
		g.write("Case #" + str(i) + ": X won" + "\n")
	elif (matrix[0][1] == 'X' or matrix[0][1] == 'T') and (matrix[1][1] == 'X' or matrix[1][1] == 'T') and (matrix[2][1] == 'X' or matrix[2][1] == 'T') and (matrix[3][1] == 'X' or matrix[3][1] == 'T'): 
		g.write("Case #" + str(i) + ": X won" + "\n")
	elif (matrix[0][2] == 'X' or matrix[0][2] == 'T') and (matrix[1][2] == 'X' or matrix[1][2] == 'T') and (matrix[2][2] == 'X' or matrix[2][2] == 'T') and (matrix[3][2] == 'X' or matrix[3][2] == 'T'): 
		g.write("Case #" + str(i) + ": X won" + "\n")
	elif (matrix[0][3] == 'X' or matrix[0][3] == 'T') and (matrix[1][3] == 'X' or matrix[1][3] == 'T') and (matrix[2][3] == 'X' or matrix[2][3] == 'T') and (matrix[3][3] == 'X' or matrix[3][3] == 'T'): 
		g.write("Case #" + str(i) + ": X won" + "\n")
	elif (matrix[0][0] == 'X' or matrix[0][0] == 'T') and (matrix[1][1] == 'X' or matrix[1][1] == 'T') and (matrix[2][2] == 'X' or matrix[2][2] == 'T') and (matrix[3][3] == 'X' or matrix[3][3] == 'T'): 
		g.write("Case #" + str(i) + ": X won" + "\n")
	elif (matrix[0][3] == 'X' or matrix[0][3] == 'T') and (matrix[1][2] == 'X' or matrix[1][2] == 'T') and (matrix[2][1] == 'X' or matrix[2][1] == 'T') and (matrix[3][0] == 'X' or matrix[3][0] == 'T'): 
		g.write("Case #" + str(i) + ": X won" + "\n")
	
	## O WON

	elif (matrix[0][0] == 'O' or matrix[0][0] == 'T') and (matrix[0][1] == 'O' or matrix[0][1] == 'T') and (matrix[0][2] == 'O' or matrix[0][2] == 'T') and (matrix[0][3] == 'O' or matrix[0][3] == 'T'): 
		g.write("Case #" + str(i) + ": O won" + "\n")
	elif (matrix[1][0] == 'O' or matrix[1][0] == 'T') and (matrix[1][1] == 'O' or matrix[1][1] == 'T') and (matrix[1][2] == 'O' or matrix[1][2] == 'T') and (matrix[1][3] == 'O' or matrix[1][3] == 'T'): 
		g.write("Case #" + str(i) + ": O won" + "\n")
	elif (matrix[2][0] == 'O' or matrix[2][0] == 'T') and (matrix[2][1] == 'O' or matrix[2][1] == 'T') and (matrix[2][2] == 'O' or matrix[2][2] == 'T') and (matrix[2][3] == 'O' or matrix[2][3] == 'T'): 
		g.write("Case #" + str(i) + ": O won" + "\n")
	elif (matrix[3][0] == 'O' or matrix[3][0] == 'T') and (matrix[3][1] == 'O' or matrix[3][1] == 'T') and (matrix[3][2] == 'O' or matrix[3][2] == 'T') and (matrix[3][3] == 'O' or matrix[3][3] == 'T'): 
		g.write("Case #" + str(i) + ": O won" + "\n")
	elif (matrix[0][0] == 'O' or matrix[0][0] == 'T') and (matrix[1][0] == 'O' or matrix[1][0] == 'T') and (matrix[2][0] == 'O' or matrix[2][0] == 'T') and (matrix[3][0] == 'O' or matrix[3][0] == 'T'): 
		g.write("Case #" + str(i) + ": O won" + "\n")
	elif (matrix[0][1] == 'O' or matrix[0][1] == 'T') and (matrix[1][1] == 'O' or matrix[1][1] == 'T') and (matrix[2][1] == 'O' or matrix[2][1] == 'T') and (matrix[3][1] == 'O' or matrix[3][1] == 'T'): 
		g.write("Case #" + str(i) + ": O won" + "\n")
	elif (matrix[0][2] == 'O' or matrix[0][2] == 'T') and (matrix[1][2] == 'O' or matrix[1][2] == 'T') and (matrix[2][2] == 'O' or matrix[2][2] == 'T') and (matrix[3][2] == 'O' or matrix[3][2] == 'T'): 
		g.write("Case #" + str(i) + ": O won" + "\n")
	elif (matrix[0][3] == 'O' or matrix[0][3] == 'T') and (matrix[1][3] == 'O' or matrix[1][3] == 'T') and (matrix[2][3] == 'O' or matrix[2][3] == 'T') and (matrix[3][3] == 'O' or matrix[3][3] == 'T'): 
		g.write("Case #" + str(i) + ": O won" + "\n")
	elif (matrix[0][0] == 'O' or matrix[0][0] == 'T') and (matrix[1][1] == 'O' or matrix[1][1] == 'T') and (matrix[2][2] == 'O' or matrix[2][2] == 'T') and (matrix[3][3] == 'O' or matrix[3][3] == 'T'): 
		g.write("Case #" + str(i) + ": O won" + "\n")
	elif (matrix[0][3] == 'O' or matrix[0][3] == 'T') and (matrix[1][2] == 'O' or matrix[1][2] == 'T') and (matrix[2][1] == 'O' or matrix[2][1] == 'T') and (matrix[3][0] == 'O' or matrix[3][0] == 'T'): 
		g.write("Case #" + str(i) + ": O won" + "\n")
	elif matrix[0].find('.') != -1 or matrix[1].find('.') != -1 or matrix[2].find('.') != -1 or matrix[3].find('.') != -1:
		g.write("Case #" + str(i) + ": Game has not completed" + "\n")
	else:
		g.write("Case #" + str(i) + ": Draw" + "\n")