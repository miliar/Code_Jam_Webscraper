def xxx(m):
	for str in m.values():
		o = str.count('O')
		x = str.count('X')
		t = str.count('T')
		if o+t == 4:
			return 'O'
		if x+t == 4:
			return 'X'
	return False

fin = open('a.in', 'r')
fout = open('a.out', 'w')

n = fin.readline()
for i in range(1, int(n)+1):
	row = {}
	col = {}
	ldi = {}
	rdi = {}
	finish = True
	
	for j in range(4):
		line = fin.readline().strip()
		row[j] = line
		if '.' in line:
			finish = False

		for k in range(4):
			if k in col:
				col[k] += line[k]
			else:
				col[k] = line[k]
			if k-j in rdi:
				rdi[k-j] += line[k]
			else:
				rdi[k-j] = line[k]
			if k+j in ldi:
				ldi[k+j] += line[k]
			else:
				ldi[k+j] = line[k]
	if i==5:
		print ldi
	ans = xxx(row)
	if not ans:
		ans = xxx(col)
	if not ans:
		ans = xxx(ldi)
	if not ans:
		ans = xxx(rdi)
			
	if not ans and not finish:
		fout.write('Case #%d: Game has not completed\n' % i)
	elif not ans and finish:
		fout.write('Case #%d: Draw\n' % i)
	else:
		fout.write('Case #%d: %s won\n' % (i, ans))
		
	fin.readline()
	
fout.close()

		