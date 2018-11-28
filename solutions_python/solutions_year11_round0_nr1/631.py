T = int(raw_input())
for i in range(T):
	line = raw_input().split()
	N = int(line[0])
	line.__delitem__(0)
	last = {1:1, -1:1} # 1: O, -1: B
	time = 0 # result
	s_run = dict(last.items())
	t_run = 0
	last_r = 0
	for j in range(N):
		new_run = False
		r = 1 if line[2*j] == 'O' else -1
		b = int(line[2*j+1])
		if (last_r != 0) and (r != last_r):
			#print "hello ###", last_r, r
			new_run = True

		t = abs(b-last[r]) + 1
		if new_run:
			#print 't run', t_run
			time += max(t - t_run, 1) # shouldn't be < 1, as a robot must wait for his friend
			t_run = max(t - t_run, 1)
		else:
			time += t
			t_run += t
		#print 'time', time, 't', t
		last[r] = b
		last_r = r
		s_run = dict(last.items())
		#print str(last)
		
	print 'Case #%d: %d' % (i+1, time)