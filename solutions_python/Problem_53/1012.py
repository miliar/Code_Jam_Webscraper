file = open("A-small-attempt0.in")

while(True):
	t = file.readline().strip()
	if(len(t) == 0):
		break
	t = int(t)
	for i in range(t+1)[1:] :
		a=file.readline().strip()
		n=int(a.split()[0])
		k=int(a.split()[1])
		n_dash=2**n
		if((k+1)%(n_dash) == 0):
			print "Case #%d: ON" % i
		else :
			print "Case #%d: OFF" % i
