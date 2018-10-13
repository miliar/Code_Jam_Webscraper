import math
fin = open("input.in", "r")
fout = open("output.txt", "w")

def palo(c):
	c = list(str(c))
	return c == c[::-1] 

def raiz(c): 
	r  = math.sqrt(c)
	if ( r - int(r) ) == 0 : return int(r)
	return -1

T = int(fin.readline().strip())
for caso in range(T):
	a,b = [int(c) for c in fin.readline().split(" ")]
	conta = 0
	for i in range(a, b+1):
		if palo(i):
			r  = raiz(i)
			if r >= 0 and palo(r) :
				conta = conta + 1
	print "Case #" + str(caso+1) + ": " + str(conta)
