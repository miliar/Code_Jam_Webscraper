def check(row, rowmax,colmax):
	for j in range(len(rowmax)):
		for k in range(len(colmax)):
			if int(row[j][k]) < rowmax[j] and int(row[j][k]) < colmax[k]:
				return False
	return True

f = open('B-large.in.txt','r')
g = open('output.txt', 'w')
C = int(f.readline())
for i in range(C):
	N, M = f.readline().strip().split(' ')
	rowmax = [0 for j in range(int(N))]
	row = []
	colmax =  [0 for j in range(int(M))]
	for j in range(int(N)):
		row.append(f.readline().strip().split(' '))
		for k in range(int(M)):
			if int(row[j][k]) > rowmax[j]:
				rowmax[j] = int(row[j][k])
	
	for j in range(int(M)):
		for k in range(int(N)):
			if int(row[k][j]) > colmax[j]:
				colmax[j] = int(row[k][j])

	if check(row, rowmax, colmax):
		g.write('Case #%d: YES\n' % (i+1))
	else:
		g.write('Case #%d: NO\n' % (i+1))