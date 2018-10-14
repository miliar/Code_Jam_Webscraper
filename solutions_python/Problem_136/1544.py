input=open("b.in")


T=int(input.readline())

for caso in range(T):
	C, F, X=map(float,input.readline().split(" "))
	cookies=0
	time=0
	cps=2
	#print C,F,X
	while True:
		if cookies<C:
			if X-cookies < C:
				time+=(X-cookies)/cps
				break
			else:
				time+=(C-cookies)/cps
				cookies=C
		else:
			if X/(cps+F)<(X-cookies)/cps:
				#compro
				cookies-=C
				cps+=F
			else:
				#no compro
				time+=(X-cookies)/cps
				break
	print "Case #"+str(caso+1)+':', time