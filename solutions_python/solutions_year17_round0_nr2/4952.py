cases = int(raw_input())

for x in range (0,cases):
	n = raw_input()
	#h = int(n[0])
	for j in range(int(n),0,-1):
		#print j
		jj = str(j)
		h = int(jj[0])
		f = False
		for y in jj:
			#print y
			if(int(y)>=h):

				f = True
				h = int(y)
			else:
				f = False
				break
		if(f):
			print "Case #"+str(x+1)+": "+str(j)
			break