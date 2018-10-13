numCases = raw_input()
for cases in xrange(int(numCases)):
	ans = raw_input()
	mat = list()
	for rows in range(4):
		row = raw_input().split(" ")
		mat.append(row)

	ans2 = raw_input()
	mat2 = list()
	for rows in range(4):
		row = raw_input().split(" ")
		mat2.append(row)

	ansProb = list()
	for colum in xrange(4):
		for colum2 in xrange(4):
			if mat[int(ans) - 1][colum] == mat2[int(ans2) - 1][colum2]:
				ansProb.append(mat2[int(ans2) - 1][colum2])

	if len(ansProb) == 0:
		print "Case #{}: Volunteer cheated!".format(cases + 1)
	elif len(ansProb) > 1:
		print "Case #{}: Bad magician!".format(cases + 1)
	else:
		print "Case #{}: {}".format(cases + 1, ansProb[0])
		#print "Ans: {}".format(mat[int(ans) - 1][colum])

	#print "Ans #1: {}".format(ans)
	#print "Mat #1: {}".format(mat)
	#print "Ans #2: {}".format(ans2)
	#print "Mat #2: {}".format(mat2)()