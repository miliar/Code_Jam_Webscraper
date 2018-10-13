t = int(raw_input())
for i in range(1,t+1):
	print "Case #%d:" %i,
	c,f,x =	raw_input().split()
	c,f,x = float(c),float(f),float(x)
	ans = x/2.0000000
	rate = 2.0000000
	hotel_cost = 0.0000000
	while True:
		hotel_cost = c/rate + hotel_cost
		rate = rate + f
		construction_cost = x/rate + hotel_cost
		if construction_cost > ans:
			break
		ans = construction_cost
	print round(ans,7)