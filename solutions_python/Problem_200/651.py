
def find_max(curr, end):
	if curr > end:
		return 0
	m = curr
	for i in xrange(curr%10, 10):
		if i == 0:
			continue
		m = max(find_max(curr*10+i, end), m)
	return m


n = int(raw_input())
for i in xrange(n):
	end = int(raw_input())
	s = ''
	print 'Case #' + str(i+1) +': ' + str(find_max(0, end))