f = open("./dataset", "rb")
ofp = open("./output", "wb")

cases = int(f.readline())
matrix=[]
print "Cases "+str(cases)

for N in range(0, cases, 1):

	n, m = [int(x) for x in f.readline().split()]
	possible = True

	for i in range(0, n, 1):
		array = [int(x) for x in f.readline().split()]
		matrix.append(array)

	for i in range(0, n, 1):
		for j in range(0, m, 1):
			zxc=True
			for x in range(0,m,1):
				if(matrix[i][x]>matrix[i][j]):
					zxc=False
					break

			if(zxc==False):
				for x in range(0, n, 1):
					if(matrix[x][j]>matrix[i][j]):
						ofp.write("Case #"+str(N+1)+": NO\n")
						possible=False						
						break
			if(possible==False):
				break
		if(possible==False):
			break
	if(possible==True):	
		ofp.write("Case #"+str(N+1)+": YES\n")
	matrix = []

f.close()
ofp.close()
