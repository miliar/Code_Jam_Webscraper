a = input();

for aa in range(a):
	rows,cols  = map(int, raw_input().split(' '))
	m = [raw_input() for y in range(rows)]

	e = [[a for a in b] for b in m]

	mimp = False
	for i in range(rows):
		for j in range(cols):
			impossible = False
			if e[i][j] == '#':
				try:
					if e[i+1][j] != '#' or e[i][j+1] != '#' or e[i+1][j+1] != '#':
						raise Exception()
				except:
					impossible = True
				else:
					e[i][j] = '/'
					e[i+1][j] = '\\'
					e[i][j+1] = '\\'
					e[i+1][j+1] = '/'
			if impossible: 
				mimp = True
	print("Case #%d:"%(aa+1))
	if mimp:
		print("Impossible")
	else:
		for i in e:
			print ''.join(i)

