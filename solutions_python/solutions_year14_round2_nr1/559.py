

def entre():
	n=int(raw_input())
	inpute=[[] for i in range(n)]
	outpute=[[] for i in range(n)]
	for j in range(n):
		k=int(raw_input())
		inp=[raw_input() for x in range(k)]
		inpute[j]=inp
	return inpute,outpute

def st(s):
	r=""
	c='*'
	for j in range(len(s)):
		if c!=s[j]:
			c=s[j]
			r+=s[j]
	return r

def nbb(s,nt):
	tt=[0 for i in range(nt)]
	c=s[0]
	n=0
	i=0
	for j in range(len(s)):
		if c!=s[j]:
			c=s[j]
			i+=1
			tt[i]=1
		else:
			tt[i]+=1
	return tt

E,S=entre()

nb=0

for T in E:
	nb+=1
	r=0
	v=""
	for i in T:
		if v!="" and v!=st(i):
			v="*"
			break
		v=st(i)
	if v=="*":
		print("Case #"+str(nb)+": "+"Fegla Won")
	else:
		tt=[nbb(j,len(v)) for j in T]
		b=0
		for x in range(len(v)):
			a=0
			for y in range(len(T)):
				a+=tt[y][x]
			a=a/len(T)
			for y in range(len(T)):
				b+=max(tt[y][x]-a,a-tt[y][x])
		print("Case #"+str(nb)+": "+str(b))