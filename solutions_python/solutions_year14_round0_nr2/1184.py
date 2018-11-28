T = int(raw_input())

results = []

for i in xrange(T):
	C, F, X = map(float, raw_input().split())
	Fold = 2
	result = 0
	if X < C:
		result += X/Fold
	else:
		while True:
			Fnew = Fold + F
			result += C/Fold
			if X/Fnew > (X-C)/Fold:
				result += (X-C)/Fold
				break
			else:
				Fold += F
	results.append(result)

"""
for i in xrange(T):
	print "Case #{0:d}: {1:.7f}".format(i+1,results[i])

"""
f = open("CookieClicker.txt", 'w')
for i in xrange(T):
	print >> f, "Case #{0:d}: {1:.7f}".format(i+1,results[i])
f.close()