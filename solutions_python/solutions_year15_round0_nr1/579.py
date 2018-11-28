f = open('input','r')
o = open('output','w')

import time
start = time.time()
T= int(f.readline()[:-1])
for Ti in range(T):
	
	#parse args
	#C = int(f.readline().strip('\n'))
	#I = int(f.readline().strip('\n'))
	Smax, array = f.readline().strip('\n').split(' ')
	N = [int(i) for i in array]
	Smax=int(Smax)
	#word = f.readline().strip('\n')
	#logic
	count = 0
	memb = 0
	result = ""
	
	for S in range(1,Smax+1):
		count += N[S-1]
		memb += max (0, S - memb - count)
		
		
		
	o.write("case #{0}: {1}\n".format(Ti+1, memb))
#conclude
o.close()