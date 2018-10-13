def program(i):
	a=map(int,raw_input().split())
	count=0
	for x in range(a[0]):
		for y in range(a[1]):
			#print x,y,(x)&(y)
			if (x)&(y)<a[2]:
				count+=1
	print "Case #%d: %d"%(i,count)

n=int(raw_input())
for x in range(n):
	program(x+1)
