import math

def entre():
	n=int(input())
	inpute=[[] for i in range(n)]
	outpute=[[] for i in range(n)]
	for i in range(n):
		s=input()
		s=s.split()
		it=[ int(s[1][x]) for x in range(int(s[0])+1)]
		inpute[i]=it
	return inpute,outpute

E,S=entre()

nb=0
for T in E:
	nb+=1
	r=0
	n=0
	for i in range(len(T)):
		if i>n and T[i]>0:
			r+=i-n
			n+=i-n
		n+=T[i]
	print("Case #"+str(nb)+": "+str(r))
