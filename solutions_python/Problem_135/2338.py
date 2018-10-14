fin = open("data.in","r")
test_cases = fin.readline()
test_cases = int(test_cases[:-1])
fout = open("data.out","w+")

for i in range(test_cases):
	final_answer = None
	answer1 = int(fin.readline()[:-1])
	matrix1 = []
	for j in range(4):
		row = fin.readline()[:-1]
		row = row.split(" ")
		matrix1.append(row)
	answer2 = int(fin.readline()[:-1])
	matrix2 = []
	for j in range(4):
		row = fin.readline()[:-1]
		row = row.split(" ")
		matrix2.append(row)
	row1 = matrix1[answer1-1]
	row2 = matrix2[answer2-1]
	counter = 0
	common_elements = list(set(row1) & set(row2))
	if len(common_elements) == 1:
		final_answer = "Case #" + `i+1` + ": " + common_elements[0] + "\n"
	elif len(common_elements)>1:
		final_answer = "Case #" + `i+1` + ": " + "Bad magician!\n"
	else:
		final_answer = "Case #" + `i+1` + ": " + "Volunteer cheated!\n"
	fout.write(final_answer)
fout.close()