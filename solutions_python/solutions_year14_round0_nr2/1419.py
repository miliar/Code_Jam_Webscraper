def read_int(f):
	return int(f.readline().strip())

def read_ints(f):
	return [int(w) for w in f.readline().strip().split()]

def read_floats(f):
	return [float(w) for w in f.readline().strip().split()]


from sys import argv


in_f = open(argv[1])

T = read_int(in_f)

for i_t in range(1, T+1):
	C, F, X = read_floats(in_f)
	total_time = 0.
	num_of_farms = 0
	n_iter = 0
	while True:
		cookies_per_sec = 2. + num_of_farms * F
		time_to_finish_no_buy = X / cookies_per_sec
		time_to_buy = C / cookies_per_sec
		time_to_finish_buy_one_more = time_to_buy + X / (cookies_per_sec + F)
		if time_to_finish_no_buy < time_to_finish_buy_one_more:
			total_time += time_to_finish_no_buy
			break
		else:
			total_time += time_to_buy
			num_of_farms += 1
		n_iter += 1
	print 'Case #%s: %.7f' % (i_t, total_time)
	# print n_iter



