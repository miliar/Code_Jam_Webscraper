__author__ = 'siddmanu'


n = int(raw_input())
case = 1
while case <= n:
	l = raw_input()
	s_max = l.split(' ')[0]
	s = l.split(' ')[1]
	count = 0
	standing = 0
	i = 0
	total = 0
	for c in s:
		x = int(c)
		if standing >= i:
			standing += x
		else:
			new_audience = i - standing
			count += new_audience
			standing += new_audience
			standing += x
		i += 1
		total += x

	print 'Case #{}: {}'.format(case, count)

	case += 1

