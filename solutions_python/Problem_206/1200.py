from __future__ import division

t = int(raw_input())
for i in xrange(1,t+1):
	d, n = [int(x) for x in raw_input().strip().split(" ")]
	# horses = {}
	max_time = 0
	for j in range(n):
		k, s = [int(x) for x in raw_input().strip().split(" ")]
		dist = d - k
		# speed = horses[k]
		time = dist / s
		if time > max_time:
			max_time = time
	max_speed = d / max_time

	print "Case #{0:}: {1:.6f}".format(i, max_speed)
	# 	if k in horses.keys():
	# 		if s < horses[k]:
	# 			horses[k] = s
	# 	else: horses[k] = s
	# pos = horses.keys().sort().reverse()
	# max_time = 0
	# for x in pos:
		# dist = d - x;
		# speed = horses[x]
		# time = speed * dist
		# if time > max_time:
		# 	max_time = time