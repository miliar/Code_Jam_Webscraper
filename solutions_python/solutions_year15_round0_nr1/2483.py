n = int(raw_input())

for i in range(1, n + 1):
	person_add = 0
	cum = 0
	s_max, s = raw_input().split(' ')
	for j in range(int(s_max) + 1):
		# print j, s[j], cum
		if cum < j and s[j] != '0':
			person_add += (j - cum)
			cum = j
		cum += int(s[j])
		# print cum
	print 'Case #%d: %d' % (i, person_add)