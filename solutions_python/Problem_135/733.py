t=int(raw_input())
for i in xrange(t):
	a=[[]]*4
	x=int(raw_input())
	for j in xrange(4):
		a[j]=map(int,raw_input().split())
	b=[[]]*4
	y=int(raw_input())
	for j in xrange(4):
		b[j]=map(int,raw_input().split())
	s=[]
	for j in a[x-1]:
		if j in b[y-1]:
			s.append(j)
	if len(s)==1:
		print "Case #%d: %d" %(i+1,s[0])
	elif len(s) == 0:
		print "Case #%d: Volunteer cheated!" %(i+1)
	else:
		print	"Case #%d: Bad magician!" %(i+1)
