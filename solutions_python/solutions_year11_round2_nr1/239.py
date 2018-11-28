#!/usr/bin/python
import sys, operator, time

lines = sys.stdin.read().split('\n')[1:]

case = 0

def wp(line):
	wins = line.count('1')

	if wins == 0:
		return 0

	loses = line.count('0')
	return float(wins) / (wins + loses)

while lines:
	case += 1
	line = lines.pop(0)
	if not line:
		continue

	team_total =  int(line)
	games = lines[:team_total]
	del lines[:team_total]

	wps = []
	print "Case #%d:" % case
	for line in games:
		wp(line)
		wps.append(wp(line))


	owps = []
	for i in range(len(games)):
		line = games[i]
		owps_cnt = 0

		owp = 0
		owp_cnt = 0
		for j in range(len(line)):
			if line[j] != '.':
				owp_line = list(games[j])
				del owp_line[i]
				owp += wp(owp_line)
				owp_cnt += 1

		if owp_cnt > 0:
			owp /= owp_cnt

		owps.append(owp)

	for i in range(len(games)):
		line = games[i]
		oowp = 0
		oowp_cnt = 0
		for j in range(len(line)):
			if line[j] != '.':
				oowp += owps[j]
				oowp_cnt += 1

		if oowp_cnt > 0:
			oowp /= oowp_cnt

		print 0.25 * wps[i] + 0.50 * owps[i] + 0.25 * oowp
