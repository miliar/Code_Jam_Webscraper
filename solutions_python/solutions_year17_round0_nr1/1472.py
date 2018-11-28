t = int(input())

for z in range(t):
	x = input().split()
	p = x[0]
	f = int(x[1])
	total = 0
	try:
		a = p.index('-')
	except:
		print ("Case #%s: %s" %(z+1,total))
		continue
	
	b = len(p)

	while (True):
		if (a+f > b):
			print ("Case #%s: IMPOSSIBLE" %(z+1))
			break
		else:
			p = p[:a] + p[a:a+f].replace('+','*').replace('-','+').replace('*','-') + p[a+f:]
			total += 1
			try:
				a = p.index('-')
			except:
				break
	
	if (p.count('-') == 0):
		print ("Case #%s: %s" %(z+1,total))
