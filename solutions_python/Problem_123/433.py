import fileinput

fi = fileinput.input()
T = int(fi.readline())

for caseN in xrange(T):
	A,N = map(int,fi.readline().strip().split())
	sizes = map(int,fi.readline().strip().split())
	sizes.sort()
	mysize=A
	answer=0
	if A==1:
		answer=N
	else:
		myind=0
		nadd=[]
		while myind < N:
			if mysize>sizes[myind]:
				mysize+=sizes[myind]
				nadd.append(0)
			else:
				toadd=0
				while mysize<=sizes[myind]:
					toadd+=1
					mysize=mysize*2-1
				mysize+=sizes[myind]
				nadd.append(toadd)
			myind+=1
		#print A
		#print sizes
		#print nadd
		for i in xrange(N):
			#print 'by adding',sum(nadd[i:]),'by throwing',N-i
			if nadd[i]==0:
				pass
			elif nadd[i]==1:
				answer+=1
			elif sum(nadd[i:]) <= N-i:
				answer+=nadd[i]
			else:
				answer+=N-i
				break
	print 'Case #'+str(caseN+1)+': '+str(answer)
