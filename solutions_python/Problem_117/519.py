import sys,os

matrix = [[0 for x in range(100)] for x in range(100)]

def readInput(filename):
	global matrix
	n = 0
	m = 0

	f = open(filename)
	lines = f.readlines()

	teste = int(lines[0])
	#print "Teste:", teste

	testNr = 1
	newTest = True
	i = 0 #linia matricii
	for line in lines[1:]:
		if testNr > teste:
			return
		line = line.strip()
		
		if newTest:
			newTest = False
			n,m = line.split()
			n = int(n)
			m = int(m)
			#print "n,m=",n,m
			continue

		j = 0 # coloana matricii
		for c in line.split():  # elementele liniei
			#print i,j
			matrix[i][j] = int(c)
			j += 1
		i += 1

		if i >= n: # trec la alt test
			i = 0
			newTest = True
			print "Case #%d:" % testNr,
			findSolution(matrix, n, m)
			cleanMatrix()
			testNr += 1
			
	f.close()

def cleanMatrix():
	for i in range(100):
		for j in range(100):
			matrix[i][j] = 0

def findSolution(matrix, n, m):
	#print "----------------",n,"x",m
	#for l in matrix:
	#	print l

	# luam fiecare element si tragem o dunga orizontala + una verticala sa vedem daca iese treaba
	for i in range(n):
		for j in range(m):
			toCheck = matrix[i][j]
			#horizCheckFailed = False
			#vertCheckFailed = False
			for i2 in range(n):  # verific linia orizontala
				if matrix[i2][j] > toCheck:
					#horizCheckFailed = True
					for j2 in range(m):  # verific linia verticala
						if matrix[i][j2] > toCheck:
							#vertCheckFailed = True
							print "NO"
							return
	print "YES"

#readInput("in.txt")
#readInput("B-small-attempt0.in")
readInput("B-large.in")