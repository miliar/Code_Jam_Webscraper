#!/usr/bin/python

from sys import stdin,stdout

# Read in input
num_problems = int(stdin.readline())

for problem_number in range(1, num_problems + 1):
    num_teams = [int(x) for x in stdin.readline().split(' ')][0]
    teams = []
    for x in range(num_teams):
        team = []
        line = stdin.readline()
        for y in range(num_teams):
            team.append(line[y])
        teams.append(team)

    print "Case #" + str(problem_number) + ":"
    teams_stats = []
    for idx in range(num_teams):
        WP = teams[idx].count('1')/(1.0*(teams[idx].count('1')+teams[idx].count('0')))
        OWP_L = []
        for o_idx in range(num_teams):
            if o_idx != idx and teams[idx][o_idx] != '.':
                my_game = teams[o_idx][idx]
                teams[o_idx][idx] = '.'
                OWP = teams[o_idx].count('1')/(1.0*(teams[o_idx].count('1')+teams[o_idx].count('0')))
                OWP_L.append(OWP)
                teams[o_idx][idx] = my_game
        OWP = sum(OWP_L)/len(OWP_L)
        teams_stats.append([WP, OWP])

    for idx in range(num_teams):
        RPI = teams_stats[idx][0] * 0.25
        RPI += teams_stats[idx][1] * 0.5
        OOWP_L = []
        for o_idx in range(num_teams):
            if o_idx != idx and teams[idx][o_idx] != '.':
                OOWP_L.append(teams_stats[o_idx][1])
        OOWP = sum(OOWP_L)/(len(OOWP_L)*1.0)
        RPI += OOWP * 0.25
        print RPI

    # Output template
