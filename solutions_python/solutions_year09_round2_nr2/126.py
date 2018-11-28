def back(t, entrada, saida, listaAux) :
	#print "Abrindo ",t
	
	if (t > 1) :
		certo = False
		for i, j in zip(saida[0:t], entrada[0:t]) :
			if (i < j) :
				return False
			if (i == j) :
				continue
			if (i > j) :
				certo = True
				break
		if t == len(entrada) :
			#print certo
			#print "-------------------"
			return certo
			
	lista = list(set(entrada))
	lista.sort()
	for alg in lista :
		if (listaAux[alg] <= 0) :
			continue
			
		saida[t] = alg
		listaAux[alg] -= 1
		#print "   - Coloquei algarismo",alg
		#print "   - Saida",saida
		#print "   - Minha lista",lista
		#print "   - Minha listaAux",listaAux
		#print "Chamando ",t+1
		if (back(t+1, entrada, saida, listaAux[:])) :
			return True
		else :
			listaAux[alg] += 1


def extra(entrada, saida, listaAux) :
	i = 0
	while i < len(listaAux) :
		if listaAux[i] > 0 and i != 0:
			alg = i
			break
		i += 1

	listaAux[0] += 1	
	listaAux[alg] -= 1
	saida[0] = alg
	
	i = 1
	j = 0
	while i < len(saida) :
		if listaAux[j] > 0 :
			saida[i] = j
			listaAux[j] -= 1
			i += 1
		else :
			j += 1
	
			
T = input()
case = 0

while case < T :
	case += 1
	n = raw_input()
	n = list(n)
	
	entrada = []
	for i in n :
		entrada.append(int(i))
	
	lista = [0]*10
	for i in entrada :
		lista[i] += 1
		
	saida = [0]*len(entrada)
	listaAux = lista[:]
	
	back(0, entrada[:], saida, listaAux)
	
	certo = False
	t = len(saida)
	for i, j in zip(saida[0:t], entrada[0:t]) :
		if (i < j) :
			break
		if (i == j) :
			continue
		if (i > j) :
			certo = True
			break
	if t == len(entrada) :
		if (certo == False) :
			lista = [0]*10
			for i in entrada :
				lista[i] += 1
				
			saida = [0]*(len(entrada)+1)
			listaAux = lista[:]
			
			extra(entrada, saida, listaAux)
	
	s = []
	for x in saida :
		s.append(str(x))
	s = ''.join(s)
	
	print "Case #%d:" % case, s
	
	