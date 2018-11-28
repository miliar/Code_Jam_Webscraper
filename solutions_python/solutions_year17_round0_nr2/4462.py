def check(a):
	t=str(a)
	p=len(t)
	prev=t[0]
	w=""
	count=0
	for f in range(1,p):
		if(t[f]<prev):
			if(count==0):
				prev=int(prev)-1
			w=w+str(prev)
			prev=str(9)
			count=count+1
		else:
			w=w+prev
			prev=t[f]
	w=w+prev
	x=lol(int(w))
	if(x==-1):
		return check(int(w))
	return int(w)
	

def lol(a):
	t=str(a)
	p=len(t)
	prev=0
	for f in range(0,p):
		if(t[f]<prev):
			return -1
		prev=t[f]
	return a



t=int(raw_input())
for a in range(0,t):
	r=int(raw_input())
	w=check(r)
	print "Case #"+str(a+1)+": "+str(w)


