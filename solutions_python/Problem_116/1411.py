"""Code written using Python 2.7.2, http://www.python.org/"""

import string

def calc(case):
	print case
	result = 'Draw'
	
	(result, gameover) = checkRows(case, result)
	if gameover:
		return result

	(result, gameover) = checkCols(case, result)
	if gameover:
		return result

	(result, gameover) = checkDiags(case, result)
	return result
	
def checkRows(case, result):
	gameover = False
	for row in case:
		orow = string.replace(row, 'T', 'O');
		xrow = string.replace(row, 'T', 'X');
		if orow == 'OOOO':
			result = 'O won'
			gameover = True
			break
		if xrow == 'XXXX':
			result = 'X won'
			gameover = True
			break
		if '.' in row:
			result = 'Game has not completed'

	return (result, gameover)

def checkCols(case, result):
	cols = []
	for i in range(0, 4):
		squares = [c[i] for c in case]
		cols = cols + [''.join(squares)]

	return checkRows(cols, result)

def checkDiags(case, result):
	diags = [''.join([case[0][0], case[1][1], case[2][2], case[3][3]])]
	diags = diags + [''.join([case[0][3], case[1][2], case[2][1], case[3][0]])]
	
	return checkRows(diags, result)
		
		

f = open('A-large.in', 'r')
lines = f.readlines()
f.close()
c = int(lines[0].split()[0])
#print c
cases = [r.strip() for r in lines[1:]]
#print cases

of = open('output_a_large.txt', 'w')

for idx in range(0, c):
	of.write('Case #%(idx)i: %(i)s\n' % {'idx': idx + 1, 'i': calc(cases[idx*5:idx*5 + 4])})

of.close()

