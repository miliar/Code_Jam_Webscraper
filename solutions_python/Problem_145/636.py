from math import *

fName = "test"
fName = "A-small-attempt1"
# fName = "A-large-practice"

fin = open(fName + ".in", 'r')
fout = open(fName + ".out", 'w')

def puiss(q):
	r = q
	k = 0
	while r%2 == 0 :
		k += 1
		r = r/2
	return abs(k),abs(r)

def generation(k,p):
	n = int(floor(log(abs(p),2)))
	return str(k-n)	

T = int(fin.readline())

for t in range(T):	
	p,q = map(int, fin.readline().strip().split('/'))
	res = ""
	if p>q or p == 0 or (p<0 and q>0) or (p>0 and q<0) or q==0:
		res = "impossible"
	else:
		k,a = puiss(q)
		print p,q
		#print k,a,p
		if a != 1:
			if p%a != 0 :
				res = "impossible"
			else:
				p = abs(p/2**k)
				res = generation(k,p)
		else:
			res = generation(k,p)			
	fout.write("Case #" + str(t+1) + ": "+ res +"\n")
	
fin.close()
fout.close()