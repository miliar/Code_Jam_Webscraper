testcases = int(raw_input(''));

for case in range(testcases):
	dest, num = raw_input('').split(' '); dest = int(dest); num = int(num);
	horses = [];
	for i in range(num):
		pos, vel = raw_input('').split(' '); pos = int(pos); vel = int(vel);
		horses.append((pos, vel));
	horses.sort()
	horses = horses[::-1];
	
	times = [-1 for i in range(num)];

	maxTime = -float('inf');
	for i in range(num):
		pos, vel = horses[i];
		curTime =  ((dest - pos) / float(vel));
		if ( curTime > maxTime ):
			maxTime = curTime;
			times[i] = curTime;
		else:
			nextHorse = i - 1;
			posDiff = pos - horses[nextHorse][0];
			relVel = vel - horses[nextHorse][1];

			relTime = posDiff/float(relVel);
			if (relTime > times[nextHorse]):
				maxTime = curTime;
				times[i] = curTime;
			else:
				times[i] = times[i-1];

	print 'Case #' + str(case+1) + ': ' + str(dest/times[-1]);
	
	# for i in  horses:
	# 	print i;