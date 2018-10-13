n=int(input())
for case in range(n) :
	d,n=[int(e) for e in input().split()]
	chevaux=[]
	reach=[]
	for _ in range(n) :
		chevaux+=[[int(e) for e in input().split()]]
	for e in chevaux :
		reach+=[(d-e[0])/e[1]]
	#print(reach)
	reach.sort()
	res=d/reach.pop()
	
	
	print("Case #"+str(case+1)+": "+str(round(res,7)))
