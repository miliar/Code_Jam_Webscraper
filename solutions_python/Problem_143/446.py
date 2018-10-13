

def entre():
	n=int(raw_input())
	inpute=[[] for i in range(n)]
	outpute=[[] for i in range(n)]
	for j in range(n):
		s=raw_input()
		s=s.split()
		inpute[j]=[int(s[0]),int(s[1]),int(s[2])]
	return inpute,outpute

E,S=entre()

nb=0
for T in E:
	nb+=1
	a,b,k=T[0],T[1],T[2]
	r=min(k,a)*(b)+min(k,b)*(a)-min(k,a)*min(k,b)
	
	for i in range(k,a):
		for j in range(k,b):
			if i&j<k:
				r+=1
	
	print("Case #"+str(nb)+": "+str(r))