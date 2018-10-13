file = open('input.txt')
n = int(file.next())

for i in range(1,n+1):
	length = int(file.next())
	naomi1 = sorted(map(float,file.next().split(' ')))
	naomi2 = list(naomi1)
	naomi2.reverse()
	ken1 = sorted(map(float,file.next().split(' ')), reverse=True)
	ken2 = list(ken1)
	war = 0
	deceitfulwar = 0
	while len(naomi1) != 0:
		if naomi1[-1] < ken1[0]:
			picked = naomi1
			naomi1 = naomi1[1:]
			ken1 = ken1[1:]
		elif naomi1[-1] > ken1[0]:
			deceitfulwar += 1
			naomi1 = naomi1[:-1]
			ken1 = ken1[1:]
		else:
			naomi1 = naomi1[:-1]
			ken1 = ken1[1:]
	
	j = 0
	k = 0
	ksize = len(ken2)
	nsize = len(naomi2)
	while j < nsize and k < ksize:
		if naomi2[j] > ken2[k]:
			j += 1
			ksize -= 1
			war += 1
		else:
			k += 1
			j += 1
	
	print 'Case #%s: %s %s' %(i, deceitfulwar, war)
		