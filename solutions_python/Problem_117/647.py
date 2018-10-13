def check(rows,m,n):
	cols_checked = []
	for row in rows:
		if '2' in row:
			#check columns
			for i in range(n):
				if row[i] == '1':
					if i not in cols_checked:
						for x in range(m):
							if rows[x][i] == '2':
								return 'NO'
						cols_checked.append(i)
	return 'YES'

file = open('B-small-attempt0.in');

numCases =  int(file.readline())
for case in range(numCases):
	sizes = file.readline()
	m,n = sizes.split()
	m = int(m)
	n = int(n)
	lines =[]
	for line in range(m):
		lines.append(file.readline().strip().split())
	print "Case #"+str(case+1)+": "+check(lines,m,n)
	
