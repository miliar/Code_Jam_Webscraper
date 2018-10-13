lines=[]
file = open('C-large.in','r')
allLines = file.readlines()
file.close()
for line in allLines:
	a = line.split()
	lines.append(a)

N=int(lines[0][0])
j=1
for count in range(1,N+1):
	seq=lines[2*count-1]
	n=int(seq[0])
	candies=lines[2*count]
	#print 'candies',candies
	ints=[int(candies[i]) for i in range(n)]
	high=max(ints);x=0
	y=sum(ints)-min(ints)
	while high<>0:
		high=high/2;x+=1
	flag=0
	while x>=0:
		sums=0
		for i in range(n):
			sums=(sums+ints[i]%2)%2
			#print 'sums,ints[i]',sums,ints[i]
			ints[i]=ints[i]/2
		if sums<>0:
			#print 1000
			flag=1
			break
		x-=1
	if flag==0:
		print 'Case #%d:' % (count),y
	else:
		print 'Case #%d:' % (count),'NO'
