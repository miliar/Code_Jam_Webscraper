j=int(raw_input())
for q in xrange(j):
	c,f,x = [float(i) for i in raw_input().split()]
	cr = 2
	t = 0.0000000
	y1 = (c/cr) + (x/(cr+f))
	y2 = x/(cr)
	# print y2,y1
	# time.sleep(3)
	while y2 > y1:
		t += c/cr
		cr += f
		#print c/cr,x/(cr+f)
		y1 = (c/cr) + (x/(cr+f))
		y2 = x/(cr)
		# print y2,y1,t,cr
		# time.sleep(3)
	t += x/cr
	print "Case #%s: %.7f"%(q+1,t)