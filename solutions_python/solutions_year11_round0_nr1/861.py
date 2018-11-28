import codecs
with codecs.open("A-large.in", "r", "utf- 8") as f:
	temp = f.readlines()
	c = 0
	for x in temp[1:]:
		c += 1
		fo = False
		fb = False
		io = 1
		ib = 1
		sum = 0
		sumb = 0
		sumo = 0
		t = x.strip().split()
#		print t
		for i in t[1:]:
			if i == 'O':
				fo = True
			elif i == 'B':
				fb = True
			elif fb:
				sum += max(abs(int(i) - ib) + 1 - sumo, 1)
#				print 'B', abs(int(i) - ib) + 1
				sumb += max(abs(int(i) - ib) + 1 - sumo, 1)
				sumo = 0

				ib = int(i)
				fb = False
#				print sum, sumb, sumo
			elif fo:
#				print 'O', abs(int(i) - io) + 1
				sum += max(abs(int(i) - io) + 1 - sumb, 1)
				sumo += max(abs(int(i) - io) + 1 - sumb, 1)
				sumb = 0
				
				fo = False
				io = int(i)
#				print sum, sumb, sumo
		print "Case #{0}: {1}".format(c, sum)
