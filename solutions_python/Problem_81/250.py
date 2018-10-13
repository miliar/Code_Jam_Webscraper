import sys

def calc_wp(team, schedule):
    win = float(schedule[team].count('1'))
    lost = float(schedule[team].count('0'))
    
    return float(win / (win + lost))

def calc_wp_ignoring(n_teams, team, schedule, team_ignore):
    win = 0.0
    lost = 0.0
    
    for i in range(n_teams):
        if i != team_ignore:
            if schedule[team][i] == '1':
                win += 1.0
            elif schedule[team][i] == '0':
                lost += 1.0
    
    return float(win / (win + lost))

def mean(a_list):
    return sum(a_list)/len(a_list)

def calc_owp(n_teams, team, schedule):
    owp_list = []
    
    for i in range(n_teams):
        if (schedule[team][i] != '.'):
            owp_list.append(calc_wp_ignoring(n_teams, i, schedule, team)) 
         
    return mean(owp_list)

def calc_oowp(n_teams, team, schedule, owp_list):
    owp = []
    
    for i in range(n_teams):
        if (schedule[team][i] != '.'):
            owp.append(owp_list[i])
            
    return mean(owp)


input = sys.stdin
cases = int(input.readline())

for case in xrange (cases):
    n_teams = int(input.readline().strip())
    
    schedule = []
    for i in range(n_teams):
        schedule.append(input.readline().strip())

    wp = []
    owp = []
    for i in range(n_teams):
        wp.append(calc_wp(i, schedule))
        owp.append(calc_owp(n_teams, i, schedule))

    print "Case #%d:" % (case + 1)
    for i in range(n_teams):
        oowp = calc_oowp(n_teams, i, schedule, owp)
        print 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp 
    
    
