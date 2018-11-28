def check(arr,NM):
	for o in range(NM[0]):
		for l in range(NM[1]):
			col=0
			row=0
			for p in range(NM[0]):
				if(arr[p][l] <= arr[o][l]):
					col=col+1
			for q in range(NM[1]):
				if(arr[o][q] <= arr[o][l]):
					row=row+1
			if(col!=NM[0] and row!=NM[1]):
				return False
	return True

f=open('B-large.in')
g=open('output','wa')
T=int(f.readline())
for p in range(T):
	NM=f.readline().split()
	NM = map(int, NM)
	arr=[]
	
	for i in range(NM[0]):
		gh=f.readline().split()
		gh=map(int,gh)
		arr.append(gh)
	#arr=map(int,arr)
	#print arr
	if(check(arr,NM)):
		g.write('Case #'+str(p+1)+': '+'YES\n')
	else:
		g.write('Case #'+str(p+1)+': '+'NO\n')
g.close()

					
		
		
		
	

