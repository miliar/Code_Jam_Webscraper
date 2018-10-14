t = int(raw_input())
for i in xrange(1, t + 1):
	n = long(raw_input())
	if n < 10:
		print "Case #{}: {}".format(i, n)
	else:
		n_str = str(n)
		n_list = []
		for digit in n_str:
			n_list.append(int(digit))
		tidy = all(n_list[i] <= n_list[i+1] for i in xrange(len(n_list)-1))
		while not tidy and n > 9:
			n -= 1
			n_str = str(n)
			n_list = []
			for digit in n_str:
				n_list.append(int(digit))
			tidy = all(n_list[i] <= n_list[i+1] for i in xrange(len(n_list)-1))
		print "Case #{}: {}".format(i, n)