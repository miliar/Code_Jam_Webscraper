import sys

num_cases = int(sys.stdin.readline().strip())

def get_cps(num_farms, cookies_per_farm):
	return 2.0 + (num_farms * cookies_per_farm)
	
def time_until_can_buy_farm(farm_cost, num_farms, cookies_per_farm):
	return farm_cost / get_cps(num_farms, cookies_per_farm)
	
"""
def solve1(farm_cost, cookies_per_farm, win_at, num_farms, time_taken, time_to_beat, time_to_win_otherwise):
	time_to_win = time_until_can_buy_farm(win_at, num_farms, cookies_per_farm)
	if time_taken + time_to_win > time_to_beat:
		# print "already took %s and going to take another %s to win, can't beat %s" % (time_taken, time_to_win, time_to_beat)
		#return time_to_beat # return more than the time to beat. hopefully no overflow...
		return time_to_win_otherwise - time_taken
	time_to_farm = time_until_can_buy_farm(farm_cost, num_farms, cookies_per_farm)
	time_to_win_by_farm = time_to_farm + solve(farm_cost, cookies_per_farm, win_at, num_farms+1, time_to_farm, min(time_to_beat, time_to_win), time_to_win)
	# print "at %s farms after spending %s and gotta beat %s: time to farm: %s, time to win: %s, time to win by farm: %s" % (num_farms, time_taken, time_to_beat, time_to_farm, time_to_win, time_to_win_by_farm)
	#return min(time_to_win_by_farm, time_to_win)
	return time_to_win_by_farm
"""

def solve(farm_cost, cookies_per_farm, win_at, num_farms, time_taken_to_get_previous_farm, time_to_win_without_farms_before):	
	total_time_spent = 0
	while True:
		time_to_win_without_farms_now = time_until_can_buy_farm(win_at, num_farms, cookies_per_farm)
		if time_taken_to_get_previous_farm + time_to_win_without_farms_now > time_to_win_without_farms_before:
			return total_time_spent - time_taken_to_get_previous_farm + time_to_win_without_farms_before
		else:
			time_to_farm = time_until_can_buy_farm(farm_cost, num_farms, cookies_per_farm)
			num_farms, time_taken_to_get_previous_farm, time_to_win_without_farms_before, total_time_spent = num_farms+1, time_to_farm, time_to_win_without_farms_now, total_time_spent+time_to_farm
				
for i in range(num_cases):
	farm_cost, cookies_per_farm, win_at = map(float, sys.stdin.readline().strip().split())

	print "Case #%s:" % (i+1),
	# print farm_cost, cookies_per_farm, win_at,
	# print
	print solve(farm_cost, cookies_per_farm, win_at, 0, 0, sys.float_info.max)
