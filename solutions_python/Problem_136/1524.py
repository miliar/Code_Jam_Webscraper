c = f = x = 0.0

def CalculateTime (l):
	global c, f, x
	if l < 0:
		l = 0

	time = 0.0
	for i in range(l):
		time += c/(2.0 + i*f)

	time += x/(2.0 + l*f)

	return time

T = int(raw_input())

for j in range(T):
	inp = raw_input().split()

	c = float(inp[0])
	f = float(inp[1])
	x = float(inp[2])

	upper = 0
	while CalculateTime(2*upper + 1) < CalculateTime(upper):
		upper = 2*upper + 1

	upper = 2*upper + 1
	lower = 0

	#Now descent
	while lower + 100 < upper:
		step = (upper - lower) / 7

		newlower = lower
		while CalculateTime(newlower + step) < CalculateTime(newlower):
			newlower = newlower + step

		lower = newlower - step
		upper = newlower + step

	#Small case: force
	smallestval = float("inf")
	for i in range(lower, upper):
		if CalculateTime(i) < smallestval:
			smallestval = CalculateTime(i)

	print("Case #%(id)s: %(val).13f" % {"id" : j+1, "val" : smallestval})

