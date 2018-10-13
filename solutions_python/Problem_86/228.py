
entrada = file('C-small-attempt2.in')
salida = file('output-attempt2.ou', 'w')

casos = int(entrada.readline())

def notaPerfecta(miRango, notasOtros):
	#Hallar una nota, tal que sea divisible entre todas las otras o sean divisible entre ella
	for i in miRango:
		esPosible = True
		for j in notasOtros:
			if (j % i == 0) or (i % j == 0):
				#Esta en armonia con el otro
				pass
			else:
				esPosible = False
		
		if esPosible:
			return i
	
	return 'NO'
				
		
for i in range(casos):
	temp = entrada.readline().split()
	
	numOtros = int(temp[0])
	rangoNotas = xrange(int(temp[1]), (int(temp[2])+1))
	
	notasOtros = map(int, entrada.readline().split())
	
	#print rangoNotas
	#print notasOtros
	
	
	aux = notaPerfecta(rangoNotas, notasOtros)
	
	salida.write('Case #%d: %s\n' % ((i+1), str(aux)))
