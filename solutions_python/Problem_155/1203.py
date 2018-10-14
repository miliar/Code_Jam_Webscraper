import sys,os

def readInput(filename):
	f = open(filename)
	lines = f.readlines()
	curentLine = 0
	nrTeste = int(lines[curentLine])
	for testu in range(nrTeste):
		curentLine +=1
		test = lines[curentLine].split()
		nr = test[0]
		lista = test[1]
		rezolva(testu, int(nr),lista)
	f.close()
		
def rezolva(testu, nr, lista):
	#print "nr=", nr
	#print "lista=", lista

	list_elem = list(lista)
	list_elem = map(int, list_elem)
	#print 'list_elem', list_elem

	sum = 0
	friends = 0
	for i in range(len(list_elem)):
		if sum<i:
			friends += i-sum
			sum = i
		sum += list_elem[i]
	#print "friends", friends

	# print output
	print "Case #%d: %d" % (testu+1, friends)
			

readInput("A-large.in")                                      
	