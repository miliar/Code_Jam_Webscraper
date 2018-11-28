n = input()
for _ in xrange(n):
	s,k = raw_input().split()
	s = int(s)
	count = 0
	now_standing = 0
	for i,sk in enumerate(k):
		sk = int(sk)
		if sk > 0:
			if i > now_standing:
				count += i - now_standing
				now_standing = i + sk
			else:
				now_standing += sk
	print "Case #%d: %d" % (_+1,count)