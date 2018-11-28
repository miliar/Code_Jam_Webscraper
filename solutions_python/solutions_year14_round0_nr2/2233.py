t=eval(input())

for i in range(t):

	the_string = input()
	c, f, x = the_string.split()
	c = eval(c)
	f = eval(f)
	x = eval(x)
	time=0
	rate=2

	while(True):
		#at current rate
		t1 = x/rate
		#if you choose to buy
		t2 = c/rate + x/(rate+f)
			
		if(t1 <= t2):
			time += t1
			break
		else:
			time += c/rate
			rate += f

		
	print("Case #"+str(i+1)+": "+str(time))
