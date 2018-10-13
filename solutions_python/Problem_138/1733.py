import sys

f = open(sys.argv[1])
T = int(f.readline())

def readFloats():
	return list(map(float, f.readline().strip().split(' ')))

for t in range(T):
	N = int(f.readline())
	naomi = sorted(readFloats())
	ken = sorted(readFloats())
	naomi2 = list(naomi)
	ken2 = list(ken)
	
	deceitfulScore = 0
	warScore = 0
	for i in range(N):
		# Deceitful War
		if ken[-1] > naomi[-1]:
			del ken[-1]
			del naomi[0]
		else:
			deceitfulScore += 1
			naomi.remove(filter(lambda x: x > ken[0], naomi)[0])
			del ken[0]
		
		# War
		if ken2[-1] < naomi2[-1]:
			del naomi2[-1]
			del ken2[0]
			warScore += 1
		else:
			ken2.remove(filter(lambda x: x > naomi2[0], ken2)[0])
			del naomi2[0]
	
	print 'Case #%d:' % (t + 1), deceitfulScore, warScore
