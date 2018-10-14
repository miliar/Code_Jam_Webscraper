def casenum(r,c):
	if r>c:
		return casenum(c,r)
	if r==1:
		return c
	if r==2:
		return c+3
	if r==3:
		return c+5
	if r==4:
		return 10

t=input()
g='Case #%d: GABRIEL'
d='Case #%d: RICHARD'
for i in xrange(t):
	[x,r,c]=[int(h) for h in raw_input().split(' ')]
	case=casenum(r,c)
	if x==1:
		print g %(i+1)
	elif x==2:
		print [d,g][(r*c)%2==0] %(i+1)
	elif x==3:
		if case in [6,8,9]:
			print g %(i+1)
		else:
			print d %(i+1)
	else:
		if case<=8:
			print d %(i+1)
		else:
			print g %(i+1)