"""
Pseudominion problem for google code jam.

Angus Fletcher 2011, day before the rapture but I hope I win anyway.
"""

import sys
import os

def owp(table, team, wrt):
	games_played = 0.0
	games_won = 0.0
	table = list(table)
	for i in range(0, len(table[team]), 1):
		if i == wrt:
			continue
		if table[team][i] == '0':
			games_played += 1
		if table[team][i] == '1':
			games_played += 1
			games_won += 1
	if games_played == 0:
		return 0.0
	return games_won / games_played

t = int(sys.stdin.readline())

for i in range(0, t, 1):
	teams_table = []
	num_teams = int(sys.stdin.readline())
	
	for team in range(0, num_teams, 1):
		teams_table.append(sys.stdin.readline().strip('\n'))
		
		
	#Compute the WP for each team.
	team_wpi = []
	for team in range(0, num_teams, 1):
		games_won = 0
		games_played = 0
		wp_score = 0.0
		for opponent in range(0, num_teams, 1):
			if teams_table[team][opponent] == '0':
				games_played += 1
			elif teams_table[team][opponent] == '1':
				games_played += 1
				games_won += 1
		wp_score = float(games_won) / float(games_played)
		team_wpi.append(wp_score)
	
	team_owps = []
	for team in range(0, num_teams, 1):
		curr_wps = []
		for opp in range(0, num_teams, 1):
			if opp != team and teams_table[team][opp] != '.':
				curr_wps.append(owp(teams_table, opp, team))
		team_owps.append(sum(curr_wps) / len(curr_wps))
	
	team_oowps = []	
	for team in range(0, num_teams, 1):
		curr_owps = []
		for opp in range(0, num_teams, 1):
			if team != opp and teams_table[team][opp] != '.':
				curr_owps.append(team_owps[opp])
		team_oowps.append(sum(curr_owps) / len(curr_owps))
	
	
	
	team_rpis = []
	for team in range(0, num_teams, 1):
		team_rpis.append(0.25 * team_wpi[team] + 0.50 * team_owps[team] + 0.25 * team_oowps[team])
	
	case_string = "Case #" + str(i + 1) + ":"
	print case_string
	for j in team_rpis:
		print j 
		