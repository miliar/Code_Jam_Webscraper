import sys

def get_cases():
	cases = sys.stdin.read().split('\n')[1:-1]
	return [map(lambda x:float(x), case.split(' ')) for case in cases]

def solve(case):
	C = case[0]
	F = case[1]
	X = case[2]

	farm_times = [float(C/2.0)]
	farm_times.append(farm_times[0] + (C / (2.0 + F)))
	times = [X/2.0]
	times.append(farm_times[0] + (X / (2.0 + F)))

	n = 1
	while times[n] < times[n-1]:
		farm_times.append(farm_times[n] + (C / (2.0 + F*(n+1))))
		times.append(farm_times[n] + (X / (2.0 + F*(n+1))))
		n += 1
	return times[n-1]

cases = get_cases()
for x in range(0,len(cases)):
	print "Case #%d: %.7f" % (x+1, solve(cases[x]))