def main():
	for TEST in xrange(1, int(raw_input())+1):
		C, F, X = map(float, raw_input().split())

		cookie_rate = 2		# cookies per second
		cumulative_time = 0
		time = X / cookie_rate

		while 1:
			old_time = time
			cumulative_time += C / cookie_rate
			cookie_rate += F
			time = cumulative_time + X / cookie_rate

			if old_time < time:
				break;

		print "Case #%d: %.7f" % (TEST, old_time)

main()
