import os




if __name__ == '__main__':

	file = open('IN', 'r')
	dati = file.read().split('\n')
	
	L = int(dati[0])
	
	dati = dati[1:-1]
	#print dati
	
	tavole = []
	
	for i in range(L):
		
		tavola = []
		for l in range(5):
			if l == 4:
				continue
			tavola.append(dati[i*5 + l])

		tavole.append(tavola)
		
	#print tavole
	
	
	for count, tavola in enumerate(tavole):
		
		print "Case #" + str(count+1) + ":",	
		
		win = False
		
		for riga in tavola:
			if riga.replace("X", "T") == "TTTT" :
				print "X won"
				win = True
				break
		
		if not win:
			for i in range(4):
				res = ""
				for riga in tavola:
					res = res + riga[i].replace("X", "T")
			
				if res == "TTTT":
					print "X won"
					win = True
				
		if not win:
			res = ""
			for l, riga in enumerate(tavola):
				res = res + riga[l].replace("X", "T")
			if res == "TTTT":
				print "X won"	
				win = True
			
		if not win:	
			res = ""
			for l, riga in enumerate(tavola):
				res = res + riga[3-l].replace("X", "T")
			if res == "TTTT":
				print "X won"	
				win = True	
	
	
	
		if not win:
			for riga in tavola:
				if riga.replace("O", "T") == "TTTT" :
					print "O won"
					win = True
					break
		
		if not win:
			for i in range(4):
				res = ""
				for riga in tavola:
					res = res + riga[i].replace("O", "T")
			
				if res == "TTTT":
					print "O won"
					win = True
				
		if not win:
			res = ""
			for l, riga in enumerate(tavola):
				res = res + riga[l].replace("O", "T")
			if res == "TTTT":
				print "O won"
				win = True	
			
		if not win:	
			res = ""
			for l, riga in enumerate(tavola):
				res = res + riga[3-l].replace("O", "T")
			if res == "TTTT":
				print "O won"
				win = True

		
		if not win:
			for riga in tavola:
				for lettera in riga:
					if lettera == ".":
						win = True
						
						
			if not win:
				print "Draw"
			else:
				print "Game has not completed"

	


					
		

