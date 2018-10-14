f = open("data.in","r")
totalcases = f.readline()
totalcases = int(totalcases[:-1])
fout = open("data.out","w+")

for i in range(totalcases):
	fal_answer = None
	ans1 = int(f.readline()[:-1])
	mat1 = []
	for j in range(4):
		row = f.readline()[:-1]
		row = row.split(" ")
		mat1.append(row)
	ans2 = int(f.readline()[:-1])
	mat2 = []
	for j in range(4):
		row = f.readline()[:-1]
		row = row.split(" ")
		mat2.append(row)
	row1 = mat1[ans1-1]
	row2 = mat2[ans2-1]
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
