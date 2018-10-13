for i in xrange(input()):
	m,r=map(str, raw_input().split())
	t=z=0
	for j in xrange(int(m)+1):
		if j<=t:
			t+=int(r[j])
		else:
			z+=1
			t+=1
			t+=int(r[j])
	print "Case #"+str(i+1)+":",z