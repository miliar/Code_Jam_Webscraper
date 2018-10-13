"""
doc
"""
from sys import stdin

def tup(n,k):
	result = []
	for i in n:
		result.append(('N',i,n.index(i)))
	for i in k:
		result.append(('K',i))
	result.sort(key = lambda x: x[1])
	return result

def dwar(n,k):
	w = 0
	values = tup(n,k)
	#print values
	for i in range(len(ken)):
		x = k.pop(0)
		if x >n[len(n)-1]:
			n.pop(0)
		else:
			for l in range(len(n)):
				if n[l] > x :
					w+=1
					n.pop(l)
					break
	#print n,k
	return w

def war(n,k):
	w = 0
	for i in range(len(n)):
		x = n.pop(0)
		if x > k[len(k)-1] :
			w += 1
			k.pop(0)
		elif x < k[0]:
			k.pop(0)
		else:
			for l in range(len(k)):
				if k[l]>x:
					k.pop(l)
					break
	return w

lines = []

T = int(stdin.readline().split()[0])

for i in range(T):
	line = stdin.readline().split()
	c = float(line[0])
	naomi = stdin.readline().split()
	ken = stdin.readline().split()
	naomi.sort()
	ken.sort()
	#print naomi, ken 
	y = dwar(naomi[:],ken[:])
	z = war(naomi[:],ken[:])
	#endtime = playgame(c,f,x)

	print "Case #"+str(i+1)+":", y,z