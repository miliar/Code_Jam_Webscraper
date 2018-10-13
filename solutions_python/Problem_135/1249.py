import sys,os

def readInput(filename):
	global matrix
	linia = 0
	coloana = 0

	f = open(filename)
	lines = f.readlines()
	curentLine = 0
	nrTeste = int(lines[curentLine])
	for testu in range(nrTeste):
		curentLine +=1
		raspuns1 = int(lines[curentLine])
		mat1 = list()
		curentLine +=1
		s = set(lines[curentLine].split())
		mat1.append(s)
		curentLine +=1
		s = set(lines[curentLine].split())
		mat1.append(s)
		curentLine +=1
		s = set(lines[curentLine].split())
		mat1.append(s)
		curentLine +=1
		s = set(lines[curentLine].split())
		mat1.append(s)

		curentLine +=1
		raspuns2 = int(lines[curentLine])
		mat2 = list()
		curentLine +=1
		s = set(lines[curentLine].split())
		mat2.append(s)
		curentLine +=1
		s = set(lines[curentLine].split())
		mat2.append(s)
		curentLine +=1
		s = set(lines[curentLine].split())
		mat2.append(s)
		curentLine +=1
		s = set(lines[curentLine].split())
		mat2.append(s)

		#print mat1
		#print mat2
		#print '------------'
		#print 'linii: ', raspuns1, raspuns2
		rezultat = mat1[raspuns1-1].intersection(mat2[raspuns2-1])
		#print 'rez=', rezultat, len(rezultat)
		print "Case #%d:" % (testu+1),
		if len(rezultat) == 1:
			print list(rezultat)[0]
		elif len(rezultat) == 0:
			print "Volunteer cheated!"
		else:
			print "Bad magician!"

	f.close()
		

readInput("input.txt")                                      
	