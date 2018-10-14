data = open("large_set.txt").readlines()
length = int(data[0])

naomi_offset = 2
ken_offset = 3
for entry in xrange(length):
	naomi = data[(entry * 3) + naomi_offset].split()
	naomi = [float(value) for value in naomi]

	ken = data[(entry * 3) + ken_offset].split()
	ken = [float(value) for value in ken]

	ken.sort()
	naomi.sort()

	ken_true = ken[:]
	naomi_true = naomi[:]

	naomi_score = 0
	naomi_true_score = 0

	nr_items = len(ken)
	for elem in xrange(nr_items):
		if ken[-1] > naomi[-1]:
			del ken[-1]
			del naomi[0]
		else:
			del ken[-1]
			del naomi[-1]
			naomi_score += 1


	for elem in xrange(nr_items):
		if ken_true[-1] > naomi_true[-1]:
			del ken_true[-1]
			del naomi_true[-1]
		else:
			del ken_true[0]
			del naomi_true[-1]
			naomi_true_score += 1


	print "Case #%i: %i %i" % ( entry + 1, naomi_score, naomi_true_score)
