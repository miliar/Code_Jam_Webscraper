def integer(n):
	return int(n)

f = open("problem1.in","r")
fout = open("problem1.out","w")
t = int(f.readline())

for case in range(1, t + 1):
	row1 = int(f.readline()) - 1
	matrix1 = []
	for i in range(0,4):
		matrix1.append(f.readline().split())
		matrix1[i] = map(integer,matrix1[i])

	row2 = int(f.readline()) - 1
	matrix2 = []
	for i in range(0,4):
		matrix2.append(f.readline().split())
		matrix2[i] = map(integer,matrix2[i])

	result = []
	for i in range(0,4):
		if(matrix1[row1][i] in matrix2[row2]):
			result.append(matrix1[row1][i])

	if(len(result) > 1):
		fout.write("Case #" + str(case) + ": Bad magician!\n")
	elif (len(result) == 1):
		fout.write("Case #" + str(case) + ": " + str(result[0]) + "\n")
	else:
		fout.write("Case #" + str(case) + ": Volunteer cheated!\n")

f.close()
fout.close()
