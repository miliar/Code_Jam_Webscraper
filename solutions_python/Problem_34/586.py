def nxt(what,border):
	what[len(what)-1]=what[len(what)-1]+1
	for i in range(len(what)-1,0,-1):
		if (what[i]>=border[i]):
			what[i]=0
			what[i-1]=what[i-1]+1
	if (what[0]>=border[0]):
		return []
	else:
		return what
f=open('in.txt','r')
ts=f.readline().split()
L=int(ts[0])
D=int(ts[1])
N=int(ts[2])
words=[]
for i in range(D):
	ts=f.readline().rstrip()
	words.append(ts)

for case in range(N):
	actSet=[]
	ts=f.readline().rstrip()
	state=0
	t=set()
	for c in ts:
		if (state==0):
			if (c=='('):
				state=1
				t=set()
			else:
				actSet.append(set(c))
		else:
			if (c==')'):
				actSet.append(t)
				state=0
			else:
				t.add(c)
	res=0
	for w in words:
		found=1
		for i in range(L):
			if (w[i] not in actSet[i]):
				found=0
		if (found==1):
			res=res+1
	print 'Case #'+str(case+1)+':',res
f.close()