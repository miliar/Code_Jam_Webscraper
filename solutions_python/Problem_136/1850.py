t = int(input())
for i in range(1, t + 1):
	print ("Case #", i, ": ", sep ='', end='')
	c, f, x = tuple(float(i) for i in input().split())
	current = 2.0
	spent = 0.0
	while True:
		need = x / current
		ifBuy = c / current + x / (current + f)
		if need > ifBuy:
			spent += c / current
			current += f
		else:
			print (spent + need)
			break

