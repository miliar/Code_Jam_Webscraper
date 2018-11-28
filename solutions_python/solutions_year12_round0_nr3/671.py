## Recycled Numbers

def crearHash(inicio, fin):
	miHash = {}
	for i in range(inicio, fin+1):
		miHash[str(i)] = []
	return miHash

def rotacionesNumero(numero):
	## Regresa todas las rotaciones del numero
	original = numero
	lista = []
	for i in range(len(numero)-1):
		lastDigit = numero[-1]
		numero = lastDigit + numero[:-1]
		if(numero[0] == "0" or (original == numero)):
			continue
		lista.append(numero)
	return lista

def resuelve(cadena):
	cadena = cadena.split(" ")
	if(len(cadena[0]) == 1):
		return 0
	start = int(cadena[0])
	end = int(cadena[1])
	miLista = crearHash(start, end)
	contador = 0
	for item in miLista:
		rotaciones = rotacionesNumero(item)
		for candidato in rotaciones:
			if(start <= int(candidato) <= end):
				candidatoList = miLista[candidato]
				if(item not in candidatoList):
					contador += 1
					candidatoList.append(item)
					itemList = miLista[item]
					itemList.append(candidato)
	return contador

## Main()
f = open("file.in", "r")
s = open("output", "w")
f.readline()
contador = 1
for linea in f:
	s.write("Case #%d: %d\n" % (contador, resuelve(linea[:-1])))
	contador += 1
f.close()
s.close()
