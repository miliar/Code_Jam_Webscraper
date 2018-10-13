import sys
rl = lambda: sys.stdin.readline().strip()

t = int(rl())
for case_number in range(t):
	x, s, r, t, n = map(int, rl().split())
	walkways = []
	walkway_total_length = 0
	running_left = 1.0 * t
	for i in range(n):
		b, e, w = map(int, rl().split())
		walkway_total_length += (e - b)
		walkways.append([b, e, w])


	for i in range(n - 1):
		for j in range(i + 1, n):
			if walkways[i][2] > walkways[j][2]:
				tmp = walkways[i]
				walkways[i] = walkways[j]
				walkways[j] = tmp

	rest_length = x - walkway_total_length
	if (1.0 * rest_length) / r <= running_left:
		time_running = (1.0 * rest_length) / r
		total_time = time_running
		running_left -= time_running
	else:
		length_running = running_left * r
		total_time = (1.0 * length_running) / r + (1.0 * (rest_length - length_running)) / s
		running_left = 0.0

#	print running_left
#	print total_time

		
	for i in range(n):
		b = walkways[i][0]
		e = walkways[i][1]
		w = walkways[i][2]

		if (1.0 * (e - b)) / (w + r) <= running_left:
			time_on_walkway = (1.0 * (e - b)) / (w + r)
			running_left -= time_on_walkway
			total_time += time_on_walkway
		else:
			length_running = running_left * (w + r)
			time_on_walkway = (1.0 * length_running) / (w + r) + (1.0 * (e - b - length_running)) / (w + s)

			total_time += time_on_walkway
			running_left = 0.0

			


	print "Case #%d: %.9f" % (case_number + 1 , total_time)

