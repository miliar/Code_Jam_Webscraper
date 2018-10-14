t = int(raw_input())

for ab in range(t):
	s_max, s = raw_input().split()
	s_max = int(s_max)

	current_count = 0
	required = 0
	for i in range(len(s)):
		value = int(s[i])
		if current_count < i and value > 0:
			required += i - current_count
			current_count += i - current_count
		current_count += value

	print "Case #%d: %d" % (ab+1, required)
