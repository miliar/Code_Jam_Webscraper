def outcome(rows):
	columns = []
	diags = []
	k = ''
	p = ''
	for i in range(4):
		s = ''
		for j in range(4):
			s += rows[j][i]
		columns.append(s)
		k += rows[i][i]
		p += rows[i][3-i]
	diags.append(k)
	diags.append(p)
	unfinished = False
	for i in rows+columns+diags:
		if '.' not in i:
			if 'O' not in i:
				return 'X won'
			if 'X' not in i:
				return 'O won'
		else:
			unfinished = True
	if not unfinished:
		return 'Draw'
	else:
		return 'Game has not completed'
		
def data(filename):
	f = open(filename,'r')
	l = f.readlines()
	for i in range(len(l)-1):
		l[i] = l[i][:-1]
	f.close()
	cases = []
	f = open(filename + ' output','w')
	for i in range(int(l[0])):
		cases.append([])
		for j in range(4):
			cases[i].append(l[1+5*i+j])
		f.write('Case #' + str(i+1) + ': ' + outcome(cases[i]) + '\n')
	f.close()