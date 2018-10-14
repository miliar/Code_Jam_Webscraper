f = open('input', 'r')

num_cases = int(f.readline().strip())

def fair_war(naomi, ken):
	points = 0
	for x in naomi:
		if ken[-1] < x:
			points += 1
			ken.pop(0)
		else:
			for index,j in enumerate(ken):
				if j > x:
					ken.pop(index)
					break
	return str(points)

def deceitful_war(naomi, ken):
	points = 0
	for x in naomi:
		for i in xrange(len(ken)):
			if(x > ken[i]):
				points += 1
				ken.pop(i)
				break
	return str(points)


for i in xrange(num_cases):
	num_blocks = int(f.readline().strip())
	naomi = map(float, f.readline().strip().split(" "))
	naomi.sort()
	ken = map(float, f.readline().strip().split(" "))
	ken.sort()
	print "Case #" + str(i+1) + ": " + deceitful_war(naomi, ken[:]) + " " + fair_war(naomi, ken)
	#print fair_war(naomi, ken[:])
	#print deceitful_war(naomi, ken)






