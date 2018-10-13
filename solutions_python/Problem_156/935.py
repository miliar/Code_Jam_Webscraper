from sys import stdin

def get_runtime(diner):
	orig = diner[0]
	divisor = diner[1]
	return orig/divisor + orig%divisor

cases = int(stdin.readline())
timelost = 1

for case in xrange(cases):
	stdin.readline()
	diners = map(lambda x: (int(x), 1), stdin.readline().split(' '))
	minutes = 0
	optruntime = -1
	while True: 
		diners.sort(reverse=True, key=get_runtime)
		runtime = get_runtime(diners[0]) + minutes
		slowest = get_runtime(diners[0])
		if (optruntime == -1 or optruntime > runtime):
			optruntime = runtime
		if (slowest == 1):
			break

		# prep for next iter
		minutes += 1
		diners[0] = (diners[0][0], diners[0][1]+1)
		

	print "Case #%d: %d" % (case+1, optruntime)

