inf = open('A-large.in', 'r')
outf = open('aAns.txt', 'w')




T = int(inf.readline())
for j in xrange(T):
	print j+1
	mas = []
	R, C = map(int, inf.readline().split())
	for i in xrange(R):	
		c = inf.readline()
		if c[-1] == '\n':
			c = c[:-1]
		mas.append(list(c))
	cant = 0
	for i in xrange(R-1):
		for ii in xrange(C-1):
			if mas[i][ii] == '#':
				if (mas[i][ii+1] == '#') and (mas[i+1][ii] == '#') and (mas[i+1][ii+1] == '#'):
					mas[i][ii] = '/'
					mas[i][ii+1] = '\\'
					mas[i+1][ii] = '\\'
					mas[i+1][ii+1] = '/'
				else:
					cant = 1
					break
	if not cant:			
		for i in xrange(R):
			if mas[i][-1] == '#':
				cant = 1
				break
	if not cant:
		for i in xrange(C):
			if mas[-1][i] == '#':
				cant = 1
 				break
	outf.write('Case #' + str(j+1) + ':\n')
	if cant == 1:
		outf.write('Impossible\n')
	else:
		for i in xrange(R):
			outf.write(''.join(mas[i]) + '\n')
	
inf.close()
outf.close()		