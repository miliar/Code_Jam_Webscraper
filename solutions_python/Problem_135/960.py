testCases = int(raw_input())
for test in range(testCases):
	guess1 = int(raw_input())
	matrix1 = [[] for i in range(4)]
	for row in range(4):
		matrix1[row] = [int(i) for i in raw_input().split(" ")]
	guess2 = int(raw_input())
	matrix2 = [[] for i in range(4)]
	for row in range(4):
		matrix2[row] = [int(i) for i in raw_input().split(" ")]
	guess1 -= 1
	guess2 -= 1
	res = []
	for i in range(4):
		flag = 0
		for j in range(4):
			if(matrix1[guess1][i] == matrix2[guess2][j]):
				flag = 1
		if flag == 1:
			res.append(matrix1[guess1][i])

	if not len(res):
		print "Case #" + str(test + 1) + ": Volunteer cheated!"
	elif len(res) == 1:
		print "Case #" + str(test + 1) + ": " + str(res[0])
	else:
		print "Case #" + str(test + 1) + ": Bad magician!"
