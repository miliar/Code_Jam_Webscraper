import bisect
t = int(input(''))
cc = 0
while True:
	t-=1
	if t < 0:
		break
	cc += 1
	c = int(input(''))
	naomi = [float(p) for p in input('').split(' ')]
	ken = [float(p) for p in input('').split(' ')]
	
	ken.sort()
	naomi.sort()
	
	#print(naomi)
	#print(ken)
	
	naomi1 = naomi[:]
	ken1 = ken[:]
	c1 = c
	
	res = 0
	while True:
		c = c-1
		if c < 0:
			break
		
		if naomi[c] > ken[c]:
			naomi.remove(naomi[c])
			ken.remove(ken[0])
			res = res + 1
		else:
			index = bisect.bisect(ken, naomi[c])
			ken.remove(ken[index])
			naomi.remove(naomi[c])

	res1 = 0
	while True:
		c1 = c1-1
		if c1 < 0:
			break
		
		if naomi1[0] < ken1[0]:
			naomi1.remove(naomi1[0])
			ken1.remove(ken1[c1])
		else:
			naomi1.remove(naomi1[0])
			ken1.remove(ken1[0])
			res1 = res1 + 1
	
	print("Case #"+ str(cc) +":", res1, res)
