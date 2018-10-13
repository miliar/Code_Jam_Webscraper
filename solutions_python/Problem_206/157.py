n_tests=int(raw_input())
for t in range(n_tests):
	s=raw_input().split(' ')
	d=int(s[0])
	n_horses=int(s[1])
	max_speed=-1
	for h in range(n_horses):
		s=raw_input().split(' ')
		intercept=int(s[0])
		slope=int(s[1])
		new_t=1.0*(d-intercept)/slope
		new_speed=1.0*d/new_t
		if max_speed<0 or new_speed<max_speed:
			max_speed=new_speed
	print('Case #%d: %f' % (t+1, max_speed))
