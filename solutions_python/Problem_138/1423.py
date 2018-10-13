def war(naomi, ken):
	points = 0
	while len(naomi) > 0:
		n = naomi.pop()
		index = 0
		for k in ken:
			if k > n:
				break
			index = (index + 1) % len(ken)
		points += (n > ken.pop(index))
	return points
	
def deceitful_war(naomi, ken):
	if naomi[0] > ken[-1]:
		return len(naomi)
	points = 0
	while len(naomi) > 0:
		index = 0
		for n in naomi:
			if n > ken[0]:
				break
			index = (index + 1) % len(naomi)
		
		if naomi.pop(index) > ken[0]:
			points += 1
			ken.pop(0)
		else:
			ken.pop()
				
	return points

for T in range(int(raw_input())):
	n = int(raw_input())
	naomi = sorted((float(weight) for weight in raw_input().split(' ')))
	ken = sorted((float(weight) for weight in raw_input().split(' ')))
	print "Case #%d: %d %d" % (T+1, deceitful_war(naomi[:], ken[:]), war(naomi[:], ken[:]))