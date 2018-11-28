
def can(ns, currentPos, changed, ret):
	if currentPos == len(ns):
		return True
	first = 1 if currentPos == 0 else ret[currentPos-1]
	last = 9 if changed else ns[currentPos]
	for digit in xrange(last, first - 1, -1):
		nextChanged = changed or digit < ns[currentPos]
		ret[currentPos] = digit
		nextCan = can(ns, currentPos+1, nextChanged, ret)
		if nextCan:
			return True
	return False


t = input()
for case in xrange(t):
	ns = map(int, list(raw_input()))
	ret = [-1]*len(ns)
	print "Case #{}:".format(case+1),
	if can(ns, 0, False, ret):
		print "".join(map(str, ret))
	else:
		print "".join(["9"]*(len(ns) - 1))
