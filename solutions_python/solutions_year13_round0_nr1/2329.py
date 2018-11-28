import os



def chequear(tablero):	
	hayBlanco=False
	for linea in range(4):
		if tablero[linea].find('.') == -1:
			if tablero[linea].find('O') == -1:
				return "X won"
			elif tablero[linea].find('X') == -1:
				return "O won"
		else:
			hayBlanco=True
	for col in range(4):
		fila= tablero[0][col] + tablero[1][col] + tablero[2][col] + tablero[3][col]
		if fila.find('.') == -1:
			if fila.find('O') == -1:
				return "X won"
			elif fila.find('X') == -1:
				return "O won"
	dia= tablero[0][0] + tablero[1][1] + tablero[2][2] + tablero[3][3]
	if dia.find('.') == -1:
		if dia.find('O') == -1:
			return "X won"
		elif dia.find('X') == -1:
			return "O won"
	dia2= tablero[0][3] + tablero[1][2] + tablero[2][1] + tablero[3][0]
	if dia2.find('.') == -1:
		if dia2.find('O') == -1:
			return "X won"
		elif dia2.find('X') == -1:
			return "O won"
	if hayBlanco:
		return "Game has not completed"
	else:
		return "Draw"

def solve(path):
	f = open(path)
	#out = open("res.out",'w')
	case = int(f.readline())
	for i in range(case):
		tablero = []
		for linea in range(4):
			tablero.append(f.readline())
		f.readline()
		print "Case #" + str(i+1)+":", chequear(tablero)

solve("A-large.in")
