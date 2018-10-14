t = int(input())
for i in range(1,t+1):
	d,n=(input()).split()
	d = float(d)
	n = int(n)
	maxtime = 0
	for j in range (0,n):
		k,s=(input()).split()
		k = float(k)
		s = float(s)
		time = (d-k)/s
		if (time > maxtime):
			maxtime = time
	realspeed = d/maxtime
	print("Case #"+str(i)+": "+str(realspeed))