num_cases = int(raw_input())
for case_num, cases in enumerate(range(num_cases)):
	n = int(raw_input())
	visited = set()
	q = []

	for i in range(1, 10):
		q.append(i)
		visited.add(i)
	
	result = 1
	while len(q) > 0:
		t = q.pop(0)
		if t <= n and t > result:
			result = t

		rem = t%10
		for i in range(rem, 10):
			t1 = t * 10 + i
			if t1 not in visited and t1 <= n:
				q.append(t1)
				visited.add(t1)
	
	print "Case #%s: %d" % (case_num+1, result)
