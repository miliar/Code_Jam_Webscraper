n_cases = int(raw_input())

def read_int():
	return int(raw_input())

for case in range(1, n_cases+1):
	C, F, X = map(float, raw_input().split())
	rate = 2.0
	time_elapsed = 0.0

	remaining_time = X / rate
	
	while True:
		new_remaining_time = X / (rate + F)
		new_farm_time = C / rate
		total_remaining_time = new_farm_time + new_remaining_time
		if (remaining_time <= total_remaining_time):
			time_elapsed += remaining_time
			break
		remaining_time = new_remaining_time
		time_elapsed += new_farm_time
		rate += F

	print "Case #%d: %1.10f" % (case, time_elapsed)
