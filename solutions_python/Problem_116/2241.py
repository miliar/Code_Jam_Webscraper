## CodeJam 2013
## Brian Hernandez

from sys import argv

codigoResultado = {}
codigoResultado["X"] = "X won"
codigoResultado["O"] = "O won"
codigoResultado["empate"] = "Draw"
codigoResultado["not completed"] = "Game has not completed"

def segundaDiagonal(tupla):
	if(tupla == (0, 3) or tupla == (3, 0) or tupla == (1, 2) or tupla == (2, 1)):
		return True

def soyAlguien(i, j, arreglo):
	if(i == j):
		arreglo[2][0] += 1
	if(segundaDiagonal((i, j))):
		arreglo[2][1] += 1
	arreglo[0][i] += 1
	arreglo[1][j] += 1

def someoneWin(vX, vO, casilla):
	entrar = False
	if(casilla == "T"):
		## revisamos primero X, luego O
		entrar = True
	if(casilla == "X" or entrar):
		## revisamos X
		for direccion in vX:
			for valor in direccion:
				if(valor == 4):
					return "X"
	if(casilla == "O" or entrar):
		## revisamos O
		for direccion in vO:
			for valor in direccion:
				if(valor == 4):
					return "O"

def solve(matriz, salida, caso):
	global codigoResultado
	banderaJuegoIncompleto = False
	casillaTirada = None
	##			  H1 H2 H3 H4	V1 V2 V3 V4	  D1 D2
	victoriaX = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0]]
	victoriaO = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0]]
	for i in range(4):
		for j in range(4):
			if(matriz[i][j] == 'X'):
				soyAlguien(i, j, victoriaX)
				casillaTirada = "X"
			elif(matriz[i][j] == 'O'):
				soyAlguien(i, j, victoriaO)
				casillaTirada = "O"
			elif(matriz[i][j] == 'T'):
				soyAlguien(i, j, victoriaX)
				soyAlguien(i, j, victoriaO)
				casillaTirada = "T"
			elif(matriz[i][j] == '.'):
				banderaJuegoIncompleto = True
				casillaTirada = "."
			## verificar si alguien ya gano
			resultado = someoneWin(victoriaX, victoriaO, casillaTirada)
			if(resultado):
				salida.write("Case #%d: %s\n" % (caso, codigoResultado[resultado]))
				return
	if(banderaJuegoIncompleto):
		## si ya revise toda la matriz y nadie gano y hay casillas vacias, entonces
		salida.write("Case #%d: %s\n" % (caso, codigoResultado["not completed"]))
	else:
		## si ya revise toda la matriz y nadie ganoy no hay casillas vacias entonces
		salida.write("Case #%d: %s\n" % (caso, codigoResultado["empate"]))

f = open(argv[1], "r")
veces = f.readline()

salida = open("salida.txt", "w")

for caso in range(int(veces)):
	matriz = []
	for i in range(4):
		matriz.append(f.readline()[:-1])
	solve(matriz, salida, caso+1)
	f.readline()

f.close()
salida.close()
