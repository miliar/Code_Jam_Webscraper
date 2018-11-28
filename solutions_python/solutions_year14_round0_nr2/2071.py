times = int(raw_input())
for delicious in range(0,times):
	C, F, X = raw_input().split(" ")
	cookies = 2
	fab = 0
	seconds = 0
	time = 0
	last = 0
	
	last = float(X)/2	
	while(1):
		seconds += float(C)/cookies
		cookies+= float(F)
		time = seconds + (float(X)/cookies)
		if(time<last):
			last = time
		elif(time>last):
			break;
	print("Case #%d: %f" %(delicious+1, last))
