import numpy

f = open('/tmp/testLawn','r')
m = f.readlines()
N = int(m[0])
lineCount = int()

lineCount += 1
for k in range(N):
	H,L = m[lineCount].split()
	H,L = int(H),int(L)

	lineCount += 1

	game = list()

	for i in range(H):
		game += [[int(a) for a in m[lineCount].split()]]
		lineCount += 1

	maxH = numpy.zeros(H)	
	maxL = numpy.zeros(L)
	for i in range(H):
		for j in range(L):
			maxH[i] = max(maxH[i],game[i][j])
			maxL[j] = max(maxL[j],game[i][j])


	err = False
	for i in range(H):
		for j in range(L):
			if game[i][j] != min(maxH[i],maxL[j]):
				#print '--> ',i,j,game[i][j],min(maxH[i],maxL[j])
				err = True
				break
		if err:
			break


	if err:
		print 'Case #'+str(k+1)+': NO'
	else:
		print 'Case #'+str(k+1)+': YES'






