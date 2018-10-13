from sys import stdin

T = int(stdin.readline())
for t in xrange(T):
	numViajes, numPuestos, numGrupos = map(int, stdin.readline().split(" "))
	
	cola = map(int, stdin.readline().split(" "))
	#for i in xrange(numGrupos):
	#	cola.append(int(stdin.readline()))
	
	ganancias=0
	for v in xrange(numViajes):
		ocupados = 0
		subidos = []
		while len(cola) > 0 :
			if ocupados + cola[0] <= numPuestos :
				ocupados += cola[0]
				subidos.append(cola[0])
				del cola[0]
			else :
				break
		
		ganancias += ocupados
		cola += subidos
	
	print "Case #%d: %d"%(t+1,ganancias)

	