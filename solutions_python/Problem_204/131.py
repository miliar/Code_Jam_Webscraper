import copy
T=int(input())
INF=10**7
for t in range(T):
	temp=input().split()
	N=int(temp[0])#the number of ingredients
	P=int(temp[1])#the number of packages of each ingredient
	Ri=[int(i) for i in input().split()]#ingredient needed to make
	Qi=[[int(j) for j in input().split()] for i in range(N)]#quantity
	
	#if t!=3:
	#	continue
	
	
	#Let's sort Ri and Qi !!!
	for i in range(N):
		Qi[i].sort()
	#print(Ri)
	#print(Qi)
	newRiqua=[]
	newRinum=[]
	while sum(Ri)!=INF*N:
		m=min(Ri)
		if m==INF:
			break
		else:
			M=Ri.index(m)
			newRiqua.append(m)
			newRinum.append(M)
			Ri[M]=INF
	#print(newRiqua)
	#print(newRinum)
	Ri=copy.deepcopy(newRiqua)
	newQi=[]
	for i in newRinum:
		newQi.append(Qi[i])
	Qi=copy.deepcopy(newQi)
	#sort end
	
	#focus on which package?
	countQi=[0 for i in range(N)]
	
	#how times
	times=1
	
	#how many make package
	ans=0
	
	#while loop end
	endflag=False
	#print(Ri)
	#print(Qi)
	#print(N)
	#print(P)
	#Lets See!
	while True:
		if Ri[0]*times*0.9 <= Qi[0][countQi[0]] <= Ri[0]*times*1.1:
			for i in range(1,N):
				while Ri[i]*times*0.9>Qi[i][countQi[i]]:
					countQi[i]+=1
					if countQi[i]==P:#end
						endflag=True#end
						break       #end 
				if countQi[i]==P:    #end
					endflag=True    #end
					break           #end
				if Ri[i]*times*1.1<Qi[i][countQi[i]]:
					times+=1
					break
				if endflag:         #end
					break           #end
			else:
				ans+=1
				for i in range(N):
					countQi[i]+=1
					if countQi[i]==P:#end
						endflag=True #end
		else:
			if Ri[0]*times*1.1<Qi[0][countQi[0]]:
				times+=1
			else:
				countQi[0]+=1
		if countQi[0]>=P:            #end
			endflag=True            #end
		if endflag:                 #end
			break                   #end
		#print(countQi[0])
		#print(ans)
	print("Case #"+str(t+1)+": "+str(ans))