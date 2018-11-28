

def entre():
	n=int(input())
	inpute=[[] for i in range(n)]
	for i in range(n):
		a=int(input())
		inpute[i]=a
	return inpute

E=entre()

nb=0
for T in E:
	nb+=1
	r=T
	n=10
	l=0
	while T*10>n:
		sr=str(r)
		if len(sr)-l-2 <= -1:
			break
		if int(sr[len(sr)-l-1])<int(sr[len(sr)-l-2]):
			r=r-n
			for x in range(l+1):
				r=r+(9-int(sr[len(sr)-x-1]))*(10**x)
			n=10
			l=0
		else:
			n=n*10
			l=l+1
	print("Case #"+str(nb)+": "+str(r))
