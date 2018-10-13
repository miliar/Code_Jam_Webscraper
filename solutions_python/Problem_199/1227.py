

def entre():
	n=int(input())
	inpute=[[] for i in range(n)]
	for i in range(n):
		a=input()
		a=a.split()
		s=[[a[0][j]] for j in range(len(a[0]))]
		inpute[i]=[s,int(a[1])]
	return inpute

E=entre()

nb=0
for T in E:
	nb+=1
	r=0
	ns=T[1]
	for x in range(len(T[0])):
		if(ns>len(T[0])-x):
			bp=True
			for y in range(len(T[0])):
				if T[0][y]==["-"]:
					bp=False
			if bp:
				print("Case #"+str(nb)+": "+str(r))
			else:
				print("Case #"+str(nb)+": IMPOSSIBLE")
			break
		if T[0][x]==["-"]:
			r=r+1
			for y in range(ns):
				if T[0][x+y]==["-"]:
					T[0][x+y]=["+"]
				else:
					T[0][x+y]=["-"]

