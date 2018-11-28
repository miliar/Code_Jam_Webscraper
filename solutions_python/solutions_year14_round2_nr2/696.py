for x in range(0,int(raw_input())):
	line = raw_input().split()
	old = int(line[0])
	new = int(line[1])
	count = 0
	highest_lotto = int(line[2])
	for old_num in range(0,old):
		for new_num in range(0,new):
			if old_num & new_num < highest_lotto:
				count += 1
	print "Case #%d: %d" % (x + 1,count)