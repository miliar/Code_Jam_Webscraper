import sys 

oF = open(sys.argv[1])

T = int(oF.readline().strip())


for i in range(T):
	current_cookies = 2.0
	time = 0
	convereged = False
	[C,F,X] = [float(a) for a in oF.readline().strip().split()]
	#print C,F,X
	if (X<C):
		print "Case #%d: %f"%(i+1,X/current_cookies)
	else:
		while not convereged:
			if ((X-C)/current_cookies <= X/(current_cookies+F)):
				time+=X/current_cookies
				convereged = True
			else:
				time+=C/current_cookies
				current_cookies+=F

			
			#print time,current_cookies,X-C/current_cookies,X/(current_cookies+F)
		print "Case #%d: %0.7f"%(i+1,time)
