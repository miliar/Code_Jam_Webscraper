for t in xrange(input()):
	temp=map(float,raw_input().split())
	C,F,X=temp[0],temp[1],temp[2]
	CR=2
	prevTime=X/CR
	prevBuyTime=0.0
	while(True):
		BuyTime=C/CR
		CR=CR+F
		cookieTime=X/CR
		Res=cookieTime+BuyTime+prevBuyTime
		if(Res<prevTime):
			Res,prevTime=0,Res
			prevBuyTime=prevBuyTime+BuyTime
		else:
			print "Case #"+str(t+1)+": %.7f" % prevTime
			break