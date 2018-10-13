s_max = None
persons = None
for i in xrange(int(raw_input())):
	s_max, persons = raw_input().split()
	answer = 0
	total = int(persons[0])
	for j in xrange(1, len(persons)):
		if total < j:
			answer += j - total
			total = j
		total += int(persons[j])
	print 'Case #' + str(i+1) + ': ' + str(answer)