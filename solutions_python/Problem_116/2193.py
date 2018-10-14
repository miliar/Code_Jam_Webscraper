def prueba(matriz,juego):
	complete = [True,True]
	done = True
	for col in range(0,16,4):
		complete = acumm("X",col,1,matriz,juego)
		if complete[0]:
			return 1
		elif not complete[1]:
			done = False
		complete = acumm("O",col,1,matriz,juego)
		if complete[0]:
			return 1
		elif not complete[1]:
			done = False
	for col in range(0,4,1):
		complete = acumm("X",col,4,matriz,juego)
		if complete[0]:
			return 1
		elif not complete[1]:
			done = False
		complete = acumm("O",col,4,matriz,juego)
		if complete[0]:
			return 1
		elif not complete[1]:
			done = False				
	complete = acumm("X",0,5,matriz,juego)
	if complete[0]:
		return 1
	if not complete[1]:
		done = False
	complete = acumm("X",3,3,matriz,juego)
	if complete[0]:
		return 1
	if not complete[1]:
		done = False
	complete = acumm("O",0,5,matriz,juego)
	if complete[0]:
		return 1
	if not complete[1]:
		done = False
	complete = acumm("O",3,3,matriz,juego)
	if complete[0]:
		return 1
	if not complete[1]:
		done = False
	if done == False:
		return 2
	else:
		return 3

def acumm(valor,inicio,sep,matriz,juego):
	sumavalor = 0
	contNo = 0;
	for res in range(inicio,(4*sep)+inicio,sep):
		if matriz[res] == valor or matriz[res] == "T":
			sumavalor += 1
		if matriz[res] == ".":
			contNo += 1
	if sumavalor == 4:
		print "Case #"+str(juego)+": "+valor+" won"
		return [True,True]#ganador
	elif contNo > 0:
		return [False,False]#inacabado
	else:
		return [False,True]#empate


def main():
	fichero = open('input.txt','r');
	num_juegos = int(fichero.readline())
	matriz = []
	juego = 1
	for linea in fichero:
		if linea != "\n":
			for col in linea[:-1]:
				matriz.append(col)
		else:
			num = prueba(matriz,juego)
			if num == 2:
				print "Case #"+str(juego)+": Game has not completed"
			elif num == 3:
				print "Case #"+str(juego)+": Draw"
			juego += 1
			matriz = []
			
	num = prueba(matriz,juego)
	if num == 2:
		print "Case #"+str(juego)+": Game has not completed"
	elif num == 3:
		print "Case #"+str(juego)+": Draw"
			
	return 0

if __name__ == '__main__':
	main()

