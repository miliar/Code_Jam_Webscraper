tests = int(raw_input())

for test in xrange(1, tests+1):
	c, f, x = map(float, raw_input().split())
	rate = 2
	time_default = x / rate
	time_build = 0
	while True:
		time_factory = c / rate + x / (rate + f) + time_build

		if time_default < time_factory or (('%.7f' % time_default) == ('%.7f' % time_factory)):
			answer = time_default
			break

		time_default = time_factory
		time_build += c / rate
		rate += f

	print 'Case #%s: %.7f' % (test, answer)

