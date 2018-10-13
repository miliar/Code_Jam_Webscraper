for c in xrange(int(raw_input())):
	n,k,b,t=map(int,raw_input().split())
	pos=map(int,raw_input().split())
	vel=map(int,raw_input().split())
	x=0
	tolift=0
	if k<=0:
		print "Case #"+str(c+1)+":",0
		continue
	for i in xrange(n-1,-1,-1):
		if (b-pos[i])/(vel[i]+0.0)<=t:
			k-=1
			x+=tolift
			if k<=0:
				break
		else:
			tolift+=1
	else:
		print "Case #"+str(c+1)+": IMPOSSIBLE"
		continue
	print "Case #"+str(c+1)+":",x
