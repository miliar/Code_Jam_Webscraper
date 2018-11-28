n = int(raw_input())
for i in xrange(1, n+1):
	result = "Case #" + str(i) + ": "
	totWood = int(raw_input())
	count1 = 0
	count2 = 0
	a = raw_input()
	b = raw_input()
	wood11 = sorted(map(float, a.split()), None, None, True)
	wood21 = sorted(map(float, b.split()), None, None, True)
	wood12 = sorted(map(float, a.split()))
	wood22 = sorted(map(float, b.split()))
	for j in xrange(0,totWood):
		if wood12[0] < wood22[0]:
			del wood12[0]
			del wood22[-1]
		else:
			del wood12[0]
			del wood22[0]
			count1 += 1
	for j in xrange(0,totWood):
		if wood11[0] > wood21[0]:
			del wood11[0]
			del wood21[-1]
			count2 += 1
		else:
			del wood11[0]
			del wood21[0]
	result += str(count1) + " " + str(count2)
	print result