## Tripletas de Googlers

def alcanzaBestNumber(score, bestNumber):
	## Nos dice con que condiciones se alcanzo el TotalScore
	# [1, 1] Uso de bestNumber, uso de TripletaEspecial
	# [1, 0] Uso de bestNumber, No uso de TripletaEspecial
	# [0, 0] No uso de bestNumber, No uso de TripletaEspecial
	respuesta = [0, 0]
	if(score < bestNumber):
		return respuesta
	if(bestNumber < 2):
		respuesta[0] = 1
		return respuesta
	minimo1 = bestNumber*3 - 4
	minimo2 = minimo1 + 1
	if(minimo1 <= score):
		respuesta[0] = 1
		if(score == minimo1 or score == minimo2):
			respuesta[1] = 1
	return respuesta

def resuelve(cadena):
	cadena = cadena.split(" ")
	theScores = cadena[3:]
	tarjetasSorpresa = int(cadena[1])
	bestNumber = int(cadena[2])
	cumplidores = 0
	for score in theScores:
		resultado = alcanzaBestNumber(int(score), bestNumber)
		if(resultado[0] == 1):
			if(resultado[1] == 0):
				cumplidores += 1
			elif(tarjetasSorpresa > 0):
				cumplidores += 1
				tarjetasSorpresa -= 1
	return cumplidores

f = open("file.in", "r")
s = open("output", "w")

f.readline()
contador = 1
for linea in f:
	s.write("Case #%d: %d\n" % (contador, resuelve(linea[:-1])))
	contador += 1
f.close()
s.close()
