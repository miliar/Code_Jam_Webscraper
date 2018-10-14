a1=[1,4,9,121,484]
t=int(raw_input())
for j in xrange(t):
	ip=raw_input().split()
	a,b=int(ip[0]),int(ip[1])
	count=0
	for i in a1:
		if i>=a and i<=b:
			count=count+1
	print "Case #%d:"%(j+1),count
