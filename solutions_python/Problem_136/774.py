
T = int(raw_input())
for t in xrange(T) :
	C,F,X = map(float,raw_input().split())
	#print C,F,X,t
	
	text = "Case #"+str(t+1)+": "
		
	rate = 2
	ans = X/rate
	time = C/rate
	total_time = C/rate

	while True :
		if ans < total_time + X/(rate+F) :
			print text+str(ans)
			break
		else : 
			#print "Buy farm!"
			rate+=F
			ans = total_time+X/rate
		#print time, total_time, rate, ans
		time = C/rate
		total_time+=time

