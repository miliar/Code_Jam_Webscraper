n=int(input())

for nb in range(n) : 

	ch,k=input().split()
	k=int(k)
	l=[e=="+" for e in ch]
	cpt=0
	imp=False
	for i in range(len(l)) :
		if l[i] == False and len(l)-i>=k:
		    for j in range(i,i+k):
		        l[j]=not l[j]
		    cpt+=1
		    #print(l)
		elif not l[i]:
		    imp=True
	#print([cpt,"Impossible"][int(imp)])

	print("Case #"+str(nb+1)+":",[cpt,"IMPOSSIBLE"][int(imp)])
