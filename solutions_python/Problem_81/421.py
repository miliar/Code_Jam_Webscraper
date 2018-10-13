import codecs

with codecs.open("A-large.in", "r", "utf- 8") as f:
	temp = f.readlines()
	c = 1
	wp = []
	owp = []
	result = []
	temp.append("1")
	size = 0
	flag = False
	for x in temp[1:]:
		x = x.strip()
		if size == 0:
			size = int(x)
			cc = size
			continue
		if cc <= 0:
			if size != 0:
				print "Case #{0}:".format(c)
				for i in xrange(size):
	#				print "wp", wp[i][0]
					sumowp = 0
					qc = 0
					for j in xrange(size):
						if i == j:
							continue
						if result[j][i] == u"1":
							sumowp += (wp[j][1] - 1) / float(wp[j][1] + wp[j][2] - 1)
							qc += 1
						elif result[j][i] == u"0":
							sumowp += wp[j][1] / float(wp[j][1] + wp[j][2] - 1)
							qc += 1
					owp.append(float(sumowp) / qc)
				for i in xrange(size):
					sumoowp = 0
					coo = 0
					for j in xrange(size):
						if i == j:
							continue
						if result[j][i] != u".":
							sumoowp += owp[j]
							coo += 1
					print 0.25 * wp[i][0] + 0.50 * owp[i] + 0.25 * sumoowp / float(coo)
			size = int(x)
			cc = size
			wp = []
			owp = []
			result = []
			c += 1
		else:
			result.append(x)
			win = 0
			lose = 0
			for y in x:
				if y == u".":
					pass
				if y == u"1":
					win += 1
				if y == u"0":
					lose += 1
#			print win / float(win + lose)
			wp.append((win / float(win + lose), win, lose))
#			t = [int(z) for z in t]
			cc -= 1
