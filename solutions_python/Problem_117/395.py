def solver(rows):
	minCol = []
	maxCol = []
	minRow = []
	maxRow = []
	columns = []
	for i in range(len(rows[0])):
		columns.append([])
	for i in range(len(rows)):
		maxRow.append(max(rows[i]))
		minRow.append(min(rows[i]))
		for j in range(len(rows[i])):
			columns[j].append(rows[i][j])
	for i in range(len(columns)):
		minCol.append(min(columns[i]))
		maxCol.append(max(columns[i]))
	for i in range(len(columns)):
		for j in range(len(rows)):
			#if rows[j][i] > max(minCol[i],minRow[j]):
			#	return False
			k = rows[j][i]
			if k < min(maxCol[i],maxRow[j]):
				return False
	return True
	
def data(filename):
	f = open(filename,'r')
	l = f.readlines()
	f.close()
	for i in range(len(l)-1):
		l[i] = l[i][:-1]
	rows = []
	j = 1
	for i in range(0,int(l[0])):
		rows.append([])
		s = l[j].split(' ')
		s = map(int,s)
		for n in range(s[0]):
			rows[i].append([])
		for k in range(s[0]):
			rows[i][k] = map(int,l[j+k+1].split(' '))
		j+=s[0]+1
	f = open(filename+' output','w')
	for i in range(len(rows)):
		s = 'Case #' + str(i+1) + ': '
		if solver(rows[i]):
			s += 'YES\n'
		else:
			s += 'NO\n'
		f.write(s)
	f.close()
	
def d1(filename):
	f = open(filename,'r')
	l = f.readlines()
	f.close()
	for i in range(len(l)-1):
		l[i] = l[i][:-1]
	rows = []
	j = 1
	for i in range(0,int(l[0])):
		rows.append([])
		s = l[j].split(' ')
		s = map(int,s)
		for k in range(s[0]):
			rows[i].append(map(int,l[j+k+1].split(' ')))
		j+=s[0]+1
	return rows
	