fin = open('a.in', 'r')
fout = open('a.out', 'w')

T = eval(fin.readline())

def fun(c, n):
	n[c] = n[c] + 1
		
def out(t, n):
	if n['X'] + n['T'] == 4:
		fout.write('Case #%d: ' % (t + 1))
		fout.write('X won\n')
		return True
	if n['O'] + n['T'] == 4:
		fout.write('Case #%d: ' % (t + 1))
		fout.write('O won\n')
		return True
	return False

for t in range(T):
	flag = True
	bd = []
	for i in range(4):
		bd.append(fin.readline())
	fin.readline()
	

	try:
		for x in range(4):
			nrow = {'X': 0, 'O': 0, 'T': 0, '.': 0}
			ncol = dict(nrow)
			nrd = dict(nrow)
			nld = dict(nrow)
			dicts = [nrow, ncol, nld, nrd]

			for y in range(4):
				fun(bd[x][y], nrow) 
				fun(bd[y][x], ncol)
				fun(bd[y][y], nrd)
				fun(bd[y][3 - y], nld)
			
			for n in dicts:
				if out(t, n):
					raise Exception
	except:
		flag = False
	

	if flag:
		fout.write('Case #%d: ' % (t + 1))
		for row in bd:
			for char in row:
				if char == '.':
					flag = False
		if flag:
			fout.write('Draw\n')
		else:
			fout.write('Game has not completed\n')
