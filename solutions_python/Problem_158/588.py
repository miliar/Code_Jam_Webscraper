

def entre():
	n=int(input())
	inpute=[[] for i in range(n)]
	outpute=[[] for i in range(n)]
	for j in range(n):
		s=input()
		s=s.split()
		inpute[j]=[int(s[0]),int(s[1]),int(s[2])]
	return inpute,outpute

E,S=entre()

nb=0
for T in E:
	nb+=1
	r=0
	if ( T[1]*T[2]%T[0]!=0 or T[0]>=7 or min(T[1],T[2])<T[0]-1 ):
		print("Case #"+str(nb)+": RICHARD")
	else:
		print("Case #"+str(nb)+": GABRIEL")