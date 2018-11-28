
def eqline(a, maximo):
	aux = max(a)
	resp = []
	for x in xrange(maximo):
		if aux != a[x]:
   			resp.append(x)
   	if resp != []:
   		return resp
   	return True

def eqcol(a,i, maximo):
	aux = a[0][i]
	for x in xrange(maximo):
		if aux != a[x][i]:
			print aux
			print a[x][i]
   			return False
   	return True



f = open("B-small-attempt0.in", 'r')
g = open("output.out", 'w')
cases = int(f.readline())
i = 0

while i<cases:

 	i = i+1
	z = f.readline()
	a = int(z.split()[0])
	b = int(z.split()[1])

	matrix = [[0 for x in xrange(b)] for x in xrange(a)]
	for x in xrange(a):
		z = f.readline()
		for y in xrange(b):
			matrix[x][y] = int(z.split()[y])

	if (a == 1) or (b == 1):
		g.write("Case #" + str(i) + ": YES" + "\n")
	else:
		flag = 0
		for x in xrange(a):
			aux = eqline(matrix[x],b)
			if aux != True:
				for x in xrange(len(aux)):
					if eqcol(matrix,aux[x],a) == False:
						if flag == 0:
							g.write("Case #" + str(i) + ": NO" + "\n")
							flag = 1
							break
		if flag == 0:
			g.write("Case #" + str(i) + ": YES" + "\n")






	
