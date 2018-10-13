testcase_count = int(input())
for testcase_index in range(testcase_count):
	d, horse_count = [int(x) for x in input().split()]
	slowest_horse_finish_time = 0
	for i in range(horse_count):
		k, s = [int(x) for x in input().split()]
		finish_time = (d - k) / s
		slowest_horse_finish_time = max(finish_time, slowest_horse_finish_time)
	speed = d / slowest_horse_finish_time
	print("Case #%d: %f" % (testcase_index + 1, speed))
	
