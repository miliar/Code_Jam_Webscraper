c = 30.50000
f = 3.14159
x = 1999.19990


def get_optimal():
	s1 = 0.0
	s2 = 0.0
	s_acc = 0.0

	cur_rate = 2.0

	while True:
		s1 = (x / cur_rate)
		s2 = (c / cur_rate) + (x / (cur_rate + f))

		if ((s1 + s_acc) <= (s2 + s_acc)):
			break

		s_acc += c / cur_rate

		cur_rate += f

	return s_acc + min(s1, s2)


data = open("large_set.txt").readlines()
length = (len(data) - 1)

for elem in xrange(length):
	c, f, x = [float(value) for value in data[elem + 1].split()]
	print "Case #%i: %f" % (elem + 1, get_optimal())
