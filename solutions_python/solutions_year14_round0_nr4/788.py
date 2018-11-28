

def entre():
	n=int(raw_input())
	inpute=[[] for i in range(n)]
	outpute=[[] for i in range(n)]
	for j in range(n):
		nb=int(raw_input())
		s=raw_input()
		s=s.split()
		na=[float(i) for i in s]
		ss=raw_input()
		ss=ss.split()
		naa=[float(i) for i in ss]
		inpute[j]=[nb,na,naa]
	return inpute,outpute

E,S=entre()

nb=0
for T in E:
	nb+=1
	r=0
	l=T[0]
	T[1].sort()
	T[2].sort()
	j=0
	i=0
	ri=0
	f=l
	while i<l and j<f:
		if T[1][i]<T[2][j]:
			i+=1
			f-=1
		else:
			i+=1
			j+=1
			ri+=1
	T[1].reverse()
	T[2].reverse()
	rj=0
	j=0
	i=0
	for j in range(l):
		if T[1][j]>T[2][i]:
			rj+=1
		else:
			i+=1
	print("Case #"+str(nb)+": "+str(ri)+" "+str(rj))