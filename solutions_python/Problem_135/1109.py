import numpy as np 


fr = open('A-small-attempt0.in', 'r')
fw = open('output.txt', 'w+')
numcases = int(fr.readline())
idline = 0

for x in xrange(1,numcases+1):
	idline += 1
	rowAr1 = int(fr.readline()) - 1
	Ar1 = []
	for x in xrange(0,4):
		rowX = fr.readline().replace('\n', '').split(' ')
		Ar1.append([int(item) for item in rowX])

	rowAr2 = int(fr.readline()) - 1
	Ar2 = []
	for x in xrange(0,4):
		rowX = fr.readline().replace('\n', '').split(' ')
		Ar2.append([int(item) for item in rowX])

	print Ar1[rowAr1]
	print Ar2[rowAr2]
	solution = []
	for item in Ar1[rowAr1]:
		if item in Ar2[rowAr2]:
			solution.append(item)

	if not solution:
		text = "Volunteer cheated!"
	elif len(solution) >= 2:
		text = "Bad magician!"
	else:
		assert len(solution) == 1
		assert solution[0] in Ar1[rowAr1]
		assert solution[0] in Ar2[rowAr2]
		text = str(solution[0])


	fw.write("Case #"+str(idline)+": "+str(text)+'\n')