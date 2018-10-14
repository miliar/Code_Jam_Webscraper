def check(arr2,NM):
	for o in range(NM[0]):
		for l in range(NM[1]):
			col=0
			row=0
			for p in range(NM[0]):
				if(arr2[p][l] <= arr2[o][l]):
					col=col+1
			for q in range(NM[1]):
				if(arr2[o][q] <= arr2[o][l]):
					row=row+1
			if(col!=NM[0] and row!=NM[1]):
				return False
	return True

f=open('B-small-attempt1.in')
g=open('output2','wa')
T=int(f.readline())
for p in range(T):
	NM=f.readline().split()
	NM = map(int, NM)
	arr2=[]
	
	for i in range(NM[0]):
		gh=f.readline().split()
		gh=map(int,gh)
		arr2.append(gh)
	#arr2=map(int,arr2)
	#print arr2
	if(check(arr2,NM)):
		g.write('Case #'+str(p+1)+': '+'YES\n')
	else:
		g.write('Case #'+str(p+1)+': '+'NO\n')
g.close()

					
		
		
		
	

