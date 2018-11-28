import os




if __name__ == '__main__':

	file = open('IN', 'r')
	dati = file.read().split('\n')
	
	L = int(dati[0])
	
	dati = dati[1:-1]
	#print dati
	
	prati = []
	
	for i in range(L):
	
		print "Case #" + str(i+1) + ":",
		
		lati = dati[0].split()
		N, M = int(lati[0]), int(lati[1])
		
		dati = dati[1:]
		
		
		prato = []
		for n in range(N):
			for m in range(M):
				prato.append(int ( dati[n].split()[m]))
		
		dati = dati[N:]
		
		
		
		for pos in range(N*M):
		
			Vpossible = True
			Opossible = True

			alt = prato[pos] #altezza

			#check oriz
			for m in range(M):
				if prato[pos - pos%M + m] > alt:
					Opossible = False
					break

		
			#check vert
			for n in range(N):
				#print "A", pos, n, pos%M + n*M
				if prato[pos%M + n*M] > alt:
					Vpossible = False
					break

	
			if not Vpossible and not Opossible:
				print "NO"
				break		

			
		else:
			print "YES"	
		
		
	
	
	
	


	


					
		

