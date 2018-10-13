
		

def bfs(adj,nei,n,ub,fl):
	#print nei,nei[ub],fl
	for i in range(0,n):
		if adj[nei[ub]][i]==1:
			if i not in nei:
				nei.append(i)
			else :
				fl=1
				return(1)
	ub=ub+1
	dd=0
	if ub!=len(nei):
		dd=bfs(adj,nei,n,ub,fl)
	if dd==1:
		return 1
	else :
		return -1


def abc():
	test=0
	test=input()
	k=0
	
	while k < test:
		adj=[]
		
		k=k+1
		n=input()
		for i in range(0,n):
			adj1=[]
			for i in range(0,n):
				adj1.append(0)
			adj.append(adj1)
		for i in range(0,n):
			var=raw_input().split()
			#print(var)
			var[0]=int(var[0])
			#print(var[0])
			for j in range(1,var[0]+1):
				adj[i][int(var[j])-1]=1
				#print i,var[j]
		for i in range(0,n):
			nei=[i]
			ub=0
		#print(nei)
			op=bfs(adj,nei,n,ub,0)
			if op==1:
				break
		nval="Case #"
		nval=nval+str(k)+": "
		if op==1:
			nval=nval+"Yes"
		else :
			nval=nval+"No"
		
		print(nval)
			
		
abc()
