n = int(raw_input())
for case in range(1, n + 1):
	line = raw_input()
	arrs = line.strip().split(' ')
	C = float(arrs[0])
	F = float(arrs[1])
	X = float(arrs[2])
	min_time = 9999999999999999.0
	base = 2.0
	base_time = 0.0
	for i in range(100000):
		min_time = min(min_time, X / base + base_time)
		base_time += C / base
		base += F
	print "Case #%d: %.7f" % (case, min_time)
