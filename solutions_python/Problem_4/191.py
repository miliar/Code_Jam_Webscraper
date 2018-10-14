fI = open('A-large.in','r')
fO = open('Asmallout','w')

# of cases

Ncases = int(fI.readline())
Nc = range(Ncases)

#each case

for x in Nc:

	N_coord = int(fI.readline())
	Nx = range(N_coord)
	
	tempA = fI.readline().split(' ')
	tempB = fI.readline().split(' ')
	#print tempA, type(tempA)
	#print tempB, type(tempB)
	for y in Nx:
		tempA[y] = int(tempA[y])
		tempB[y] = int(tempB[y])
	tempA.sort()
	tempA.reverse()
	tempB.sort()
	print tempA, type(tempA)
	print tempB, type(tempB)
	indexA = 0
	indexB = 0

	sump = 0
	for y in Nx:
		sump = sump + int(tempA[y]) * int(tempB[y])
		print sump
	print sump
	temp = 'Case #' + str(x+1) + ': ' + str(sump) + '\n'
	print temp
	fO.write(temp)

fI.close()
fO.close()
