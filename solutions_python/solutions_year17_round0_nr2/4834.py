def is_tidy(number):
	last = None
	while number>0:
		mod = number % 10
		number = int(number / 10)
		if last == None:
			last = mod
		if mod > last:
			return False
		last = mod
	return True

t = int(raw_input())

for i in xrange(1, t + 1):
	m = int(raw_input())
	actual_input = m
	while actual_input >=1:
		if is_tidy(actual_input):
			break
		actual_input = actual_input - 1
	print "Case #{0}: {1}".format(i,actual_input)

