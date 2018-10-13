t=input()#110011
for i in xrange(t):
	a,b=raw_input().split()
	stand=0
	req=0
	for j in xrange(len(b)):
		if j<= stand:
			stand+=int(b[j])
		elif int(b[j]) != 0:
			req+=j-stand
			stand=int(b[j])+j
	print "Case #%d: %d" %(i+1,req)
