input = open('B-large.in', 'r')
cases = int(input.readline())
output = open("output.txt", 'w')
for i in range(cases):
	data = []
	size = input.readline().split()
	nlines = int(size[0])
	mintegers = int(size[1])

	for j in range(nlines):
    		data.append([])
		numbers = input.readline().split()
		for k in range(mintegers):
			data[j].append(int(numbers[k]))
	deletion = False
	while((nlines > 1) and (mintegers > 1)):
		minimum = data[0][0]
		rowmin = 0
		colmin = 0
		for j in range(nlines):
			for k in range(mintegers):
				if(data[j][k] < data[rowmin][colmin]):
					minimum = data[j][k]
					rowmin = j
					colmin = k
		rowsame = True
		colsame = True
		for j in range(mintegers):
			if(data[rowmin][j] != minimum):
				rowsame = False
				break
		for j in range(nlines):
			if(data[j][colmin] != minimum):
				colsame = False
				break	
		if((not colsame) and (not rowsame)):
			output.write("Case #" + str(i + 1) + ": NO\n")
			deletion = True
			break
		if(colsame):
			mintegers -= 1
			for j in range(nlines):
				del data[j][colmin]
		else:	
			del data[rowmin]
			nlines -= 1
	if not deletion: output.write("Case #" + str(i + 1) + ": YES\n")
input.close()
output.close()
