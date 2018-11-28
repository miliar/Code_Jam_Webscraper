def copying(l,p,x):
	for i in range(p,len(l)):
		l[i]=x
def check(l):
	for i in range(1,len(l)):
		if l[i]<l[i-1]:
			return False
	return True
		
t=int(raw_input())
for k in range(t):
	n=list(map(int,raw_input()))
	for i in range(len(n)-1,0,-1):
		if check(n)==True: break
		if n[i]>=n[i-1]: copying(n,i-1,n[i-1])
		else:
			n[i-1]-=1
			copying(n,i,9)
	st=''.join(map(str,n))
	if st[0]=='0': print "Case #%d: %s" % (k+1,st[1:])
	else: print "Case #%d: %s" % (k+1,st)
