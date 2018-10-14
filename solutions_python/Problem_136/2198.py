for i in range(input()):
	c,f,x = map(float,raw_input().strip().split())
	t = 0.0
	cr = 2.0
	while x/(cr+f) + c/cr <= x/cr:
		t+=c/cr
		cr+=f
	t+=x/cr
	print "Case #"+str(i+1)+":",round(t,7)