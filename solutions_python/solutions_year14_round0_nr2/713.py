f = open('B-large.in')
fw = open('B-large-output.txt', 'w')

cases = int(f.readline())
for case in range(cases):
	C, F, X = map(float, f.readline().split())
	speed = 2
	acc_time = 0
	best_time = X / speed
	while True:
		new_time = acc_time + (C / speed) + (X / (speed + F))
		if new_time < best_time:
			acc_time += C / speed
			speed += F
			best_time = new_time
		else:
			break
	
	print '%.7f' % best_time
	fw.write('Case #' + str(case + 1) + ': %.7f\n' % best_time)

fw.close()
f.close()
