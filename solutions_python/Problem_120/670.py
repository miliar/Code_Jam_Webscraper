T=int(raw_input())
for i in xrange(T):
	ip=raw_input().split()
	r,t=int(ip[0]),int(ip[1])
	if t<(2*r+1):
		print "Case #%d:"%(i+1),0
	else:
		t-=(2*r+1)
		count=0
		while t>=0:
			t-=(2*r+1+4*(count+1))
			count+=1
		print "Case #%d:"%(i+1),count

