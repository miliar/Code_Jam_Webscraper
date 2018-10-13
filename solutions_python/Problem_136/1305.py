import os, sys
import itertools
lines = [line.strip() for line in open("%s" % sys.argv[1]).readlines()]
lines.reverse()
cases = lines.pop()
for case in range(int(cases)):
	cost_of_farm, extra_cookies, cookies_to_win = map(float,lines.pop().split(" "))
	farms, time_for_farms, prev_time_to_win = [], 0, cookies_to_win/2.0
	while True:
		cookies_per_minute = (2.0 + (len(farms) * extra_cookies))
		farms.append((cost_of_farm/cookies_per_minute))
		time_to_win = time_for_farms + (cookies_to_win/cookies_per_minute)
		time_for_farms = sum(farms)
		if time_to_win > prev_time_to_win:
			break
		prev_time_to_win = time_to_win
	print "Case #%s: %s" % (case+1, prev_time_to_win)
