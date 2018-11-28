def solve(rows,matrices):
	same=[]
	for i in range(2):
		row=rows[i]
		same.append(matrices[i][row-1])
	res=[]
	for i in range(4):
		if same[0][i] in same[1]:
			res.append(same[0][i])
	if len(res)==0:
		return 'Volunteer cheated!'
	elif len(res)>1:
		return 'Bad magician!'
	else:
		return str(res[0])

n=input()
k=1
while k<=n:
	rows=[]
	matrices=[]
	for i in range(2):
		m=input()
		rows.append(m)
		matrix=[]
		for j in range(4):
			matrix.append(map(int,raw_input().split(' ')))
		matrices.append(matrix)
	print 'Case #%d: %s'%(k,solve(rows,matrices))
	k+=1