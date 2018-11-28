#Codejam QR
#Problem D. Deceitful War
#Submitted By : Yogendra Tank[yogendra1911@gmail.com]

cases = input()
for case in range(cases):
	turns = input()
	N = map(float,raw_input().split())
	K = map(float,raw_input().split())
	N.sort()
	K.sort()
	ansA = 0
	ansB = 0
	N2 = N[:]
	K2 = K[:]
	for t in range(turns):
		if N[-1]>K[-1]:
			k = K[0]
			K.remove(k)
			n = 0
			for i in N:
				if i > k:
					n=i
					break
			N.remove(n)
			ansA +=1
		else:
			N.remove(N[0])
			K.remove(K[-1])
	f = 0
	for i in range(turns):
		if (f==1): break
		for k in K2:
			if k > min(N2):
				N2.remove(N2[0])
				K2.remove(k)
				break
			else: ansB+=1
				
			if len(K2)==0:f=1				

	print 'Case #'+str(case+1)+':',ansA,len(N2)
