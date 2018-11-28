T = input()
for x in xrange(T):
	row = input()
	s1 = set()
	for i in xrange(4):
		nums = map(int, raw_input().strip().split())
		if i + 1 == row:
			s1 |= set(nums)

	row = input()
	s2 = set()
	for i in xrange(4):
		nums = map(int, raw_input().strip().split())
		if i + 1 == row:
			s2 |= set(nums)

	s = s1 & s2
	if len(s) == 0:
		ans = "Volunteer cheated!"
	elif len(s) > 1:
		ans = "Bad magician!"
	else:
		ans = str(list(s)[0])

	print "Case #%d: %s" % (x+1, ans)
