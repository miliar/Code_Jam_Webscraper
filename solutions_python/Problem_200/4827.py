import sys
f=sys.stdin
t=int(f.readline())
c=1
while t:
	t-=1
	n=int(f.readline())
	last=0
	for x in range(1,n+1):
		p=''.join(sorted(str(x)))
		if x==int(p):last=x
	print("Case #%d: %d" % (c,last))
	c+=1
