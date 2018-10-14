import sys
to = int(raw_input())
for nn in range(to):
	s=map(int,raw_input().split())
	l=s[0]
	t=s[1]
	n=s[2]
	c=s[3]
	a=[]
	dist=[]
	vals=[]
	for i in range(4,len(s)):
		a.append(s[i])
	for i in range(n):
		dist.append(a[i%c])
	ssum=0
	tt=t
	for i in range(n):
		if tt==0:
			vals.append(dist[i]*2)
		else:
			tmp=tt-dist[i]*2
			if tmp>0:
				vals.append(0)
				tt=tt-dist[i]*2
			else:
				vals.append((-1)*tmp)
				tt=0
	toso=[(vals[i],dist[i]) for i in range(n)]
	toso=sorted(toso)
###	print vals
	ll=l
	res=0
	for i in range(n-1,-1,-1):
		if ll==0 or toso[i][0]==0:
			res=res+toso[i][1]*2
		else:
			if toso[i][0]==toso[i][1]*2:
				res=res+toso[i][1]
				ll-=1
			else:
				res=res+toso[i][0]/2+2*toso[i][1]-toso[i][0]
				ll-=1
	sys.stdout.write("Case #%d: %d\n"%(nn+1,res))



