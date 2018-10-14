from __future__ import division
import sys

def get_score(t):
    return t[1]

def get_team(t):
    return t[0]

def filter_team(elem):
    if (elem[0] != t1):
        return elem

def rpi_result(wp, owp, oowp):
    return (((0.25)*wp) + ((0.5)*owp) + ((0.25)*oowp))

def has_played(elem):
    if (elem[0] == t1):
        return True
    else:
        return False

def new_or(x, y):
    return x or y

out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline().strip('\n'))
num_cases += 1

for c in range(1, num_cases):
    case = 'Case #' + str(c) + ':\n'
    out_file.write(case)

    num_teams = int(in_file.readline().strip('\n'))
    scheadule = dict()
    wp = []
    owp = []
    oowp = []

    for t in range(0, num_teams):
        line = in_file.readline().strip('\n')
        scheadule[t] = []
        acum = 0
        size2 = 0

        for p in range(0, num_teams):
            if (t != p):
                if (line[p] != '.'):
                    scheadule[t].append((p, int(line[p])))
                    acum += int(line[p])
                    size2 += 1

        wp.append(acum / size2)

    for t1 in range(0, num_teams):
        play_out_wp = []
        
        for t2 in range(0, num_teams):
            if (t1 != t2):
                if (reduce(new_or, map(has_played, scheadule[t2]))):
                    play_out_games = filter(filter_team, scheadule[t2])
                    play_out_wp.append(sum(map(get_score, play_out_games)) / len(play_out_games))

        if (play_out_wp):
            owp.append(sum(play_out_wp) / len(play_out_wp))

    for t3 in range(0, num_teams):
        acum2 = 0
        size = 0
        
        for t4 in range(0, num_teams):
            if (t3 != t4):
                t1 = t3
                if (reduce(new_or, map(has_played, scheadule[t4]))):
                    acum2 += owp[t4]
                    size += 1
                
        out_file.write(str(rpi_result(wp[t3], owp[t3], (acum2 / size))) + '\n')

        
