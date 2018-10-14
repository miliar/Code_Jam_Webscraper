def cookie(kase):
	print "Case #" + str(kase) + ":",
	
	c,f,x=tuple(map(float,raw_input().split(" ")))
	
	time=0.
	speed=2.
	while True:
		timeNext=x/speed
		timeBuy=c/speed
		timeAmortise=c/f
		if timeNext>timeBuy+timeAmortise:
			time+=timeBuy
			speed+=f
		else:
			time+=timeNext
			break
	print time
	
k=input()
for p in range(k):
	cookie(p+1)
