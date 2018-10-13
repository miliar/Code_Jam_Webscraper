t = input()
i=1
for x in range(t):
	C,F,X = map(float,raw_input().split())
	cr = 2.0
	ct = 0.0
	while (X/cr)>((C/cr)+(X/(cr+F))):
		ct+=(C/cr)
		cr+=F
	
	ct+=X/cr
	
	print "Case #"+str(i)+": "+str(round(ct,7))
	i+=1