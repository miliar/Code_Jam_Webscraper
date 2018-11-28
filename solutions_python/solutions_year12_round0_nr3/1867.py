# Carlos Sanchez Lopez
from sys import stdin
t = int(stdin.readline()) # leer entrada
d = set([]) # set vacio

for caso in range(1, t+1):
	a,b = stdin.readline().split()
	min, max = int(a), int(b)
	r = range(min, max+1)
	for i in r:
		l = len(str(i))
		s = str(i)*2
		for x in range(0, l-1):
			tok1 = s[x:l+x]
			for y in range(x+1, l):
				tok2 = s[y:l+y]
				n,m = (int(tok1), int(tok2))
				if n!=m and (n,m) not in d and n>=min and n<=max and m>=min and m<=max:
					d.add((n,m))
					d.add((m,n))
	print "Case #%d: %d" % (caso, len(d)/2)
	d = set([]) # se vacia set