fin = open("input.in", "r")
fout = open("output.txt", "w")
mensaje = ["X won", "O won", "Draw", "Game has not completed"]

n = int(fin.readline().strip())
tablero = [[] for i in range(n)]
res = [-1]*n

for caso in range(n):
	for I in range(4):
		linea = fin.readline().strip()
		tablero[caso].append(linea)
		if ('XXXT' == linea) or ('XXXX' == linea) or  ('TXXX' == linea):
			res[caso] = mensaje[0]
		elif ('OOOT' == linea) or ('OOOO' == linea) or ('TOOO' == linea):
			res[caso] = mensaje[1]
	if res[caso] < 0:
		v = [] 
		for i in range(4): 
			v.append([l[i] for l in tablero[caso]])
		d1 = [tablero[caso][i][i] for i in range(4)]
		d2 = [tablero[caso][i][ 3 - i ] for i in range(4)]
		xwon = [ list(s) for  s in ['XXXT', 'XXXX', 'TXXX'] ]
		owon = [list(s) for s in ['OOOT', 'OOOO', 'TOOO'] ]
		if any( [ xx == cc for cc in v for xx in xwon ]): 
			res[caso] = mensaje[0]
		elif any( [ oo == cc for oo in owon for cc in v ]): 
			res[caso] = mensaje[1]
		elif any( [ xx == d1 for xx in xwon ]) or any( [ xx == d2 for xx in xwon ]):
			res[caso] = mensaje[0]
		elif any( [ oo == d1 for oo in owon ]) or any( [ oo == d2 for oo in owon ]):
			res[caso] = mensaje[1]
		elif any([('.' in ll) for ll in tablero[caso]]):
			res[caso] = mensaje[3]
		else: res[caso] = mensaje[2]

	print "Case #" + str(caso+1) + ": " + str(res[caso])
	fin.readline()