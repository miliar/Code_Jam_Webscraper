import os, math

def isPali(n):
	n = str(n)
	
	if n == n[::-1]:
		return True
	else:
		return False


if __name__ == '__main__':

	file = open('IN', 'r')
	dati = file.read().split('\n')
	
	L = int(dati[0])
	
	dati = dati[1:-1]
	#print dati
	
	prati = []
	
	for count in range(L):
	
		
		
		results = 0
		
		lati = dati[0].split()
		A, B = int(lati[0]), int(lati[1])
		
		dati = dati[1:]
		
		
		a = int(math.ceil(math.sqrt(A)))
		b = int(math.floor(math.sqrt(B)))
		
		#looking for palindormes
		for i in range(a,b+1):
			if isPali(i) :
				#print i,"is pali"
				
				if isPali(i*i) :
					#print i*i,"is pali as well !!!"
					results = results + 1
				
		print "Case #" + str(count+1) + ":", results

