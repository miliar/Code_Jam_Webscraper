testCases = int(raw_input())
for test in range(testCases):
	n = int(raw_input())
	naomi = [float(i) for i in raw_input().split()]
	ken = [float(i) for i in raw_input().split()]
	naomi.sort()
	ken.sort()
	naomiScore1 = 0
	k = 0
	for i in range(n):
		if naomi[i] > ken[k]:
			naomiScore1 += 1
			k += 1
	#print naomiScore1
	k = 0
	naomiScore2 = 0
	i = 0
	while i < n:
		if len(ken) - k <= 0:
			break
		if naomi[i] < ken[k]:
			ken.remove(ken[k])
			i += 1
		elif naomi[i] > ken[k]:
			k += 1
	naomiScore2 = k
	#print naomiScore2
	print "Case #" + str(test + 1) + ": " + str(naomiScore1) + " " + str(naomiScore2)
