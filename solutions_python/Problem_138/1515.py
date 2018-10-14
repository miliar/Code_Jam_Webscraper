DEBUG=False
from itertools import permutations

input=open("d.in")
T=int(input.readline())

def cualjuega(K,valor):
	if valor>K[-1]:
		return K[0]
	for i in range(len(K)):
		if valor<K[i]:
			return K[i]

for caso in range(1,T+1):
	input.readline()
	N=map(float,input.readline().strip().split(' '))
	K=map(float,input.readline().strip().split(' '))
	K.sort()
	N.sort()
	if DEBUG:
		print K
		print N

	war=0
	Kp=K[:]
		
	for i in N:
		j=cualjuega(Kp,i)
		Kp.remove(j)
		if j<i:
				war+=1
	
	if DEBUG: print war

	dwar=0
	K
	while len(N)>0:
		if N[-1]>K[-1]:
			N.remove(N[-1])
			K.remove(K[-1])
			dwar+=1
		else:
			N.remove(N[0])
			K.remove(K[-1])

	if DEBUG: print dwar
	print "Case #"+str(caso)+":", dwar, war