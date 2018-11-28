def war(naomi, ken):
	naomi = sorted(naomi, reverse = True)
	ken = sorted(ken,reverse = True)
	
	total = 0
	
	for n in naomi:
		found = False
		for k in ken:
			if k>n:
				ken.remove(k)
				found = True
				break
		if not found:
			total+=1
		
	return total


def deceitful3(naomi, ken, l):
	naomi = sorted(naomi, reverse = True)
	ken = sorted(ken, reverse = True)
	
	maximum = 0
	#basically i try all possibilities with a little wit.
	for tries in range(l):
		local_max = 0
		for i in range(l):
			if naomi[i]>ken[i]: local_max +=1
		
		if local_max>maximum: maximum = local_max
		
		try:
			naomi = [naomi[-1]]+naomi[:-1]
		except:
			naomi = [naomi[-1]]+[naomi[:-1]]
	
	return maximum
	


f = open('D-large.in', 'r')
case_no = 1
for game in range(int(f.readline())):
	
	length = int(f.readline()[:-1])
	naomi_ = map(float, f.readline()[:-1].split(' '))
	ken_ = map(float, f.readline()[:-1].split(' '))
	
	print 'Case #'+str(case_no)+': '+str(deceitful3(naomi_, ken_, length))+' '+str(war(naomi_,ken_))
	
	case_no+=1
