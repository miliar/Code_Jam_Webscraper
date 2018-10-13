f=open(r'A_smallinput.in', 'r')
n=f.readline()
n=n.rsplit( )[0]
n=int(n)
for i in range(1, n+1) :
	line=f.readline()
	line=line.rstrip("\n\r ")	
	line=line.split(' ')
	time=0
	count=int(line.pop(0))
	curr = {}
	next = {}
	curr['B']=1
	curr['O']=1
	# print curr
	for j in range(1, count+1):
		priority=line.pop(0)
		next[priority]=int(line.pop(0))
		if priority=='B': other='O'
		else : other='B'
		err=0
		time=time+abs(next[priority]-curr[priority])+1
		# print time
		try : x=line.index(other)
		except ValueError : 
			err=1
			curr[other]=0
			next[other]=0
		if err!=1 : 
			next[other]=int(line[x+1])
		if next[other] != 0 :
			if abs(next[other]-curr[other]) <= (abs(next[priority]-curr[priority])+1) : 
				curr[other]=next[other]
			else: 
				if(next[other] > curr[other]) : curr[other]=curr[other] + abs(next[priority]-curr[priority])+1
				else : curr[other]=curr[other]-abs(next[priority]-curr[priority])-1
		curr[priority]=next[priority]
		# print "next is ",next
	print 'Case #{0}: {1}'.format(i, time)
