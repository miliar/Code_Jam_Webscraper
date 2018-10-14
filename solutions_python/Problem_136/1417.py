for case_num in range (1,int(raw_input()) + 1):
	line = raw_input().split()
	cookies_per_farm = float(line[0])
	increase_per_farm = float(line[1])
	cookies_needed = float(line[2])
	cookies_per_second = 2.0

	seconds_for_current_rate = cookies_needed / cookies_per_second
	seconds_for_next_rate = cookies_per_farm / cookies_per_second + (cookies_needed / (cookies_per_second + increase_per_farm))
	total_seconds = 0.0
	while seconds_for_current_rate > seconds_for_next_rate:
		total_seconds += cookies_per_farm / cookies_per_second
		cookies_per_second +=  increase_per_farm
		seconds_for_current_rate = cookies_needed / cookies_per_second
		seconds_for_next_rate = cookies_per_farm / cookies_per_second + (cookies_needed / (cookies_per_second + increase_per_farm))
	print 'Case #%d: %s' % (case_num , total_seconds + cookies_needed / cookies_per_second)