import math

def entre():
	n=int(input())
	inpute=[[] for i in range(n)]
	outpute=[[] for i in range(n)]
	for i in range(n):
		s=input()
		s=s.split()
		inpute[i]=[int(s[0]),int(s[1]),int(s[2])]
	return inpute,outpute

E,S=entre()

nb=0
for T in E:
	nb+=1
	r=int(T[2]+T[0]*(T[1]/T[2]))
	if T[1]%T[2]==0 or T[2]==1:
		r-=1
	print("Case #"+str(nb)+": "+str(r))
