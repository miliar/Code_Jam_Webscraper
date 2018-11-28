T = raw_input()

for i in xrange(int(T)):
	temp = raw_input()
	temp = temp.split(' ')

	smax, s =temp
	s = list(s)
	count = 0
	friends = 0

	for j in xrange(len(s)):
		if count < j:
			friends += j - count
			count += j - count + int(s[j])
		else:
			count += int(s[j])
	print "Case #{}: {}".format(i + 1, friends)