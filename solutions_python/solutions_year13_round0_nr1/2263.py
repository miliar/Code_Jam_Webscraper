def create_list(n):
	lista = []
	for i in range(n):
		l2 = []
		for j in range(4):
			l2.append(raw_input())
		lista.append(l2)
		
		if(i < n - 1):
			raw_input()

	return lista
	



def verify(l, x, y, ix, iy, c):
	i = 0
	while(i < 4):
		if(l[y][x] != c) and (l[y][x] != 'T'):
			return 0
		x += ix
		y += iy
		i += 1
	return 1

def check_game(l):
	for i in range(4):
		#colunas
		a = verify(l, i, 0, 0, 1, 'X')
		if(a != 0):
			return "X won"

		a = verify(l, i, 0, 0, 1, 'O')
		if(a != 0):
			return "O won"


		#linhas
		a = verify(l, 0, i, 1, 0, 'X')
		if(a != 0):
			return "X won"

		a = verify(l, 0, i, 1, 0, 'O')
		if(a != 0):
			return "O won"


		#diagonais
		a = verify(l, 0, 0, 1, 1, 'X')
		if(a != 0):
			return "X won"

		a = verify(l, 0, 0, 1, 1, 'O')
		if(a != 0):
			return "O won"

		a = verify(l, 0, 3, 1, -1, 'X')
		if(a != 0):
			return "X won"

		a = verify(l, 0, 3, 1, -1, 'O')
		if(a != 0):
			return "O won"


	for i in range(4):
		for j in range(4):
			if(l[i][j] == '.'):
				return "Game has not completed"

	return "Draw"




l = create_list(input())
for i in range(len(l)):	
	print "Case #" + str(i + 1) + ": " + str(check_game(l[i]))