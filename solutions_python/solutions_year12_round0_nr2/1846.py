import string

f=open(r'B_smallinput.in', 'r')
n=f.readline()
n=n.rsplit( )[0]
n=int(n)
for i in range(1, n+1) :
	line=f.readline()
	line=line.rstrip("\n\r ")
	line=line.split(' ')
	count=int(line.pop(0))
	s=int(line.pop(0))
	p=int(line.pop(0))
	l = []
	
	# print count, s, p
	for j in xrange(0,count):
		l.append(int(line.pop(0)))
	# print l
	
	surprises = 0
	ans = 0
	for j in xrange(0,count):
		if (l[j] == 3*p-4 or l[j] == 3*p-3) and p-2>0 :
			surprises+=1
		if l[j] >= 3*p-2:
			ans+=1

	if s <= surprises:
		ans+=s
	else:
		ans+=surprises
	
	print 'Case #{0}: {1}'.format(i, ans)
