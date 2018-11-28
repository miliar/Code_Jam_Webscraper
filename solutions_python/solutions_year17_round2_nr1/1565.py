t = input()
for uidsi in range(1,t+1):
	d = raw_input()
	d = d.split(" ")

	n = int(d[1])
	d = float(d[0])

	t = []
	for i in range(0,n):
		ki = raw_input()
		ki = ki.split(" ")
		si = float(ki[1])
		ki = float(ki[0])
		ki = d - ki
		t.append(float(ki/si))

	min_t = float(max(t))
	
	a_t = float(d/min_t)
	print "Case #"+str(uidsi)+": "+str(a_t)