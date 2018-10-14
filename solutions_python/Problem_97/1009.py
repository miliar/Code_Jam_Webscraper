def wei(a):
	count=0
	while(a!=0):
		a=a/10
		count+=1
	return count
	
def test(a,l,b,u):
	c=b
	tt=[]
	temp=b
	tt.append(b)
	for j in range(wei(b)):
		c=c%(10**(wei(c)-1))*10+c/10**(wei(c)-1)
		if(c>=l and c<=u):
			if(c!=temp):
				if ([max(temp,c),min(temp,c)] not in a) and (c not in tt):
#					a.append([max(temp,c),min(temp,c)])
					tt.append(c)
					temp=c
	if(len(tt)>=2):
		for j in tt:
			for k in tt:
				if j<k:
					if([j,k] not in a):
						a.append([j,k])
ff=file('C-small-attempt0.in','r')
T = int(ff.readline())
for t in range(1,T+1):
	a=[]
	ll,uu=map(int,ff.readline().split())
	for i in range(ll,uu+1):
		test(a,ll,i,uu)
	print "Case #%d: %d" % (t,len(a))

ff.close()
			