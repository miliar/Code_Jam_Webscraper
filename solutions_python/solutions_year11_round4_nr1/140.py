def airport():
	t = int(raw_input())
	for case in xrange(1,t+1):
		x,s,r,t,n = map(float,raw_input().split())
		n = int(n)	
		beta = {}
		speeds = set()
		w = x
		for i in xrange(0,n):
			a,b,speed = map(int,raw_input().split())
			dist = b-a
			w -= dist
			if speed in beta:
				beta[speed] += dist
			else:
				beta[speed] = dist
			speeds.add(speed)
		speeds = sorted(speeds)
		#total running time is t
		# distance left to cover is left
		t = float(t)
		left = float(x)
		time_taken = float(0)
		#first let him run on no elevators
#		print 'r - ',r,'t - ',t
		if r*t > w:
			t = t - w/r
			time_taken += w/r
		else:
			dist_run = r*t
			dist_left_to_walk = w - dist_run
			time_taken += t + dist_left_to_walk/s
			t = 0
		left = left - w
#		print 'w - ',w,'beta - ',beta,' time_taken - ',time_taken,'speeds - ',speeds
#		print 'dist_left - ',left
		#now only elevators are left
		for speed in speeds:
			dist = beta[speed]
			if (r+speed)*t > dist:
				t = t - dist/(r+speed)
				left = left - dist
				time_taken += dist/(r+speed)
			else:
				dist_run = (r+speed)*t
				dist_left_to_elevate = dist - dist_run
				time_taken += t + dist_left_to_elevate/(speed+s)
				t = 0	
		print 'Case #'+str(case)+': '+str(time_taken)

airport()
