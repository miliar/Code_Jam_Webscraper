number_of_test_case = int(raw_input())
t = 1
while t <= number_of_test_case:
	raw_input()
	c_list = [int(c) for c in raw_input().strip().split()]
	c_list.sort()
	x_sum = 0
	for c in c_list:
		x_sum ^= c
	if x_sum == 0:
		print 'Case #%d: %d' % (t, sum(c_list[1:]),)
	else:
		print 'Case #%d: NO' % (t,)
	t += 1

