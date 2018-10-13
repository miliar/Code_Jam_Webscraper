t=input()
for i in range(t):
	a=map(str,raw_input().split())
	sum=0
	k=int(a[1][0])
	for j in range(1,len(a[1])):
		if k+sum<j:
			sum+=1
		k+=int(a[1][j])
	print "Case #%d: %d" % (i+1,sum)			
