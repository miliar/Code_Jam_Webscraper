def get_times (times):
	l = times[0].split(':')
	k = times[1].split(':')
	return (int(l[0])*60+int(l[1]),int(k[0])*60+int(k[1])) 

cases = int(raw_input())
for k in xrange (0, cases):
	tt = int(raw_input())
	(na,nb) = [int(n) for n in raw_input().split(' ')]
	db_a = {}
	db_b = {}
	leave_a = []
	leave_b = []
	for i in xrange (0, na):
		times = raw_input().split(' ')
		(t1, t2) = get_times (times)
		if t2+tt in db_a: db_a[t2+tt] += 1
		else: db_a[t2+tt] = 1
		leave_a.append (t1);
	for i in xrange (0, nb):
		times = raw_input().split(' ')
		(t1, t2) = get_times (times)
		if t2+tt in db_b: db_b[t2+tt] += 1
		else: db_b[t2+tt] = 1
		leave_b.append (t1)

	count_a = 0
	count_b = 0
	for i in leave_a:
		max_local = 0
		for j in db_b:
			if j <= i and j > max_local and db_b[j] >= 1:
				max_local = j
		if max_local == 0:
			count_a += 1
		else:
			db_b[max_local] -= 1;
	for i in leave_b:
		max_local = 0
		for j in db_a:
			if j <= i and j > max_local and db_a[j] >= 1:
				max_local = j
		if max_local == 0:
			count_b += 1
		else:
			db_a[max_local] -= 1;
	print 'Case #' + str(k+1) + ':', count_a, count_b
