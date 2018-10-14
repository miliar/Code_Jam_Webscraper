
#def fun(a, maximo):
#	aux = max(a)
#	resp = []
#	for x in xrange(maximo):
#		if aux != a[x]:
#  			resp.append(x)
#   	if resp != []:
#   		return resp
#   	return True



f = open("A-small-attempt0.in", 'r')
g = open("output.out", 'w')
cases = int(f.readline())
i = 0

while i<cases:

 	i = i+1
	raw1 = int(f.readline())
#	a = int(z.split()[0])
#	b = int(z.split()[1])

	matrix1 = [[0 for x in xrange(4)] for x in xrange(4)]
	for x in xrange(4):
		z = f.readline()
		for y in xrange(4):
			matrix1[x][y] = int(z.split()[y])

	raw2 = int(f.readline())
#	a = int(z.split()[0])
#	b = int(z.split()[1])

	matrix2 = [[0 for x in xrange(4)] for x in xrange(4)]
	for x in xrange(4):
		z = f.readline()
		for y in xrange(4):
			matrix2[x][y] = int(z.split()[y])

	count = 0
	answer = -1
	for x in matrix1[raw1-1]:
		if x in matrix2[raw2-1]:
			count = count + 1
			answer = x
	if count == 1:
		g.write("Case #" + str(i) + ": " + str(answer) + "\n")
	elif count > 1:
		g.write("Case #" + str(i) + ": " + "Bad magician!" + "\n")
	else:
		g.write("Case #" + str(i) + ": " + "Volunteer cheated!" + "\n")





	# if (a == 1) or (b == 1):
	# 	g.write("Case #" + str(i) + ": YES" + "\n")
	# else:
	# 	flag = 0
	# 	for x in xrange(a):
	# 		aux = eqline(matrix[x],b)
	# 		if aux != True:
	# 			for x in xrange(len(aux)):
	# 				if eqcol(matrix,aux[x],a) == False:
	# 					if flag == 0:
	# 						g.write("Case #" + str(i) + ": NO" + "\n")
	# 						flag = 1
	# 						break
	# 	if flag == 0:
	# 		g.write("Case #" + str(i) + ": YES" + "\n")






	
