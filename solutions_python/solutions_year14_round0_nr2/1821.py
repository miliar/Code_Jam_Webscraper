import decimal
decimal.getcontext().prec = 7
case=int(input())
z=1
while case>=z:
	s=input()
	s=s.split(' ')
	c=float(s[0])
	f=float(s[1])
	x=float(s[2])
	price=2+f
	time_past=(x/2)
	time_fut=(c/2)
	while (time_fut+(x/price))<time_past:
		time_past=(time_fut+(x/price))	
		time_fut+=(c/price)
		price+=f
	print("Case #"+str(z)+": ","%.9f" % time_past)
	z+=1
		
	
	
	
