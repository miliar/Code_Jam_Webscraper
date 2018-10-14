t = int(raw_input())
for i in xrange(1, t + 1):
	n, m = [int(s) for s in raw_input().split(" ")]
	l = [n]
	for j in xrange(1, m + 1):
		l.sort()
		select_value = l.pop()
		if select_value % 2 == 0:
			max_set = select_value / 2
			min_set = max_set - 1
		else:
			max_set = int(select_value / 2)
			min_set = max_set

		l.append(max_set)
		l.append(min_set)

	print "Case #{}: {} {}".format(i, max_set, min_set)
		  
		 
