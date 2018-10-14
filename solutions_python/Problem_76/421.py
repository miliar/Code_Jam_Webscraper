# python 3
T=int(input())
for t in range(1,T+1):
	N=int(input())
	val=[int(x) for x in input().split()]
	val.sort()
	sommexor=0
	somme=0
	for i in val:
		sommexor=sommexor^i
		somme+=i
	if sommexor==0: print("Case #"+str(t)+":",somme-val[0])
	else : print("Case #"+str(t)+": NO")