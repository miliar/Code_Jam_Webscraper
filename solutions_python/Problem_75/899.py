
def vaciarLista(lista):
	while (len(lista) > 0):
		del lista[0]

def fusionRepetidos(lista, combinaciones):
	if (len(lista) >= 2):
		if (lista[-1]+lista[-2] in combinaciones):
			temp = lista[-1]+lista[-2]
			del lista[-1]
			lista[-1] = combinaciones[temp]
			return True
		elif (lista[-2]+lista[-1] in combinaciones): 
			temp = lista[-2]+lista[-1]
			del lista[-1]
			lista[-1] = combinaciones[temp]
			return True
	return False


def quitarOpuestos(lista, opuestos, i):
	if len(lista) >= 2:
		for k in lista:
			temp1, temp2 = k+i, i+k
			if (temp1 in opuestos) or (temp2 in opuestos):
				vaciarLista(lista)
	

entrada = file('B-large.in')
salida = file('output-fixed-large.ou', 'w')
casos = int(entrada.readline())

baseElements = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']

for i in range(casos):
	temp = entrada.readline().split()
	
	combinaciones = {}
	cont = 1
	while (len(combinaciones) < int(temp[0])):
		combinaciones[temp[cont][0]+temp[cont][1]] = temp[cont][-1]
		cont += 1
	
	opuestos = []
	aux = 1
	while (len(opuestos) < int(temp[cont])):
		opuestos.append(temp[aux + cont])
		aux += 1
	
	secuencia = list(temp[aux+cont+1])
	
	resultado = []
	
	for w in secuencia:
		resultado.append(w)
		if not fusionRepetidos(resultado, combinaciones):
			quitarOpuestos(resultado, opuestos, w)
			
	uno = '[' + ', '.join(resultado) + ']'
	print uno
	salida.write("Case #%d: %s\n" % ((i+1), uno))
	
	#print resultado
	
	
salida.close()
