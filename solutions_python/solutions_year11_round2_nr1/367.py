def calc_wnl(team):
    wins = team.count('1')
    losses = team.count('0')
    return wins, losses

def calc_wp(one_wnl):
    w, l = one_wnl
    return 1.0 * w / (w + l)

def calc_owp(team, wnl):
    total_filtered_wp = 0.0
    count = 0
    for i, opp in enumerate(team):
        opp_wins, opp_losses = wnl[i]
        if opp == '0':
            opp_wins -= 1
            total_filtered_wp += 1.0 * opp_wins / (opp_wins + opp_losses)
            count += 1
        elif opp == '1':
            opp_losses -= 1
            total_filtered_wp += 1.0 * opp_wins / (opp_wins + opp_losses)
            count += 1
    return total_filtered_wp / count

def calc_oowp(team, owp):
    total_owp = 0.0
    count = 0
    for i, opp in enumerate(team):
        if opp in '01':
            total_owp += owp[i]
            count += 1
    return total_owp / count

def solve(teams):
    wnl = [calc_wnl(team)
           for team in teams]
    #print wnl

    wp = [calc_wp(one_wnl)
           for one_wnl in wnl]
    #print wp

    owp = [calc_owp(team, wnl)
           for team in teams]
    #print owp

    oowp = [calc_oowp(team, owp)
           for team in teams]
    #print oowp

    solution = [wp[i]/4 + owp[i]/2 + oowp[i]/4 
                for i in xrange(len(teams))]
    return solution

T = int(raw_input())
for t in xrange(1, T+1):
    N = int(raw_input())
    teams = [raw_input().strip() for _ in xrange(N)]
    solution = solve(teams)
    print "Case #%d:" % t
    print "\n".join(str(f) for f in solution)
