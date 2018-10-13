import math
a=int(raw_input())
for i in range(1,a+1):
	s=raw_input()
	ss=s.split(" ")
	b=int(ss[0])
	c=int(ss[1])
	count=0
	for j in range(b,c+1):
		sq=int(math.sqrt(j))
		if(j==(sq*sq)):
			st=int(str(j)[::-1])
			sqst=int(str(sq)[::-1])
			if(st==j and sqst==sq):
				count=count+1


	print "Case #%d: %d"%(i,count)

