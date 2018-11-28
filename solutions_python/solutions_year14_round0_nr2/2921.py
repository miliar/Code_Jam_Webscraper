f1=file("./outB.out","w+")
t = int(input())
for i in xrange(1,t+1):
	cookies = 0
	seconds = 0.0
	time =0
	rate = 2
	aux = raw_input().split(" ")
	c = float(aux[0])
	f = float(aux[1])
	x = float(aux[2])
	mini = x/rate
	while True:
		seconds +=c/rate
		rate +=f
		time=seconds+(x/rate)
		if time<mini:
			mini = time
		else:
			break
	print >>f1, "Case #%d: %.7f" % (i,mini)