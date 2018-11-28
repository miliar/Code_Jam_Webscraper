n_test = int(raw_input())

for t in xrange(1, n_test + 1):
	dig_n = map(lambda c: ord(c) - ord('0'), list(str(raw_input())))
	
	next_dig = 9
	tidy_n = ""
	for c in reversed(dig_n):
		if c > next_dig:
			tidy_n = chr(ord('0') + c - 1) + '9' * len(tidy_n)
			next_dig = c - 1
		else:
			tidy_n = chr(ord('0') + c) + tidy_n
			next_dig = c

	print "Case #" + str(t) + ": " + tidy_n.lstrip('0')