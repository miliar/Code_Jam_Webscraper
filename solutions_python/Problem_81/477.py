from fractions import Fraction as F

def parse(N, schedule):
    games = {}
    for team1, row in enumerate(schedule):
        for team2, c in enumerate(row):
            if c == '1':
                games[(team1, team2)] = 1
            elif c == '0':
                games[(team1, team2)] = 0
    return games

def calc_wp(N, games):
    wp = {}
    for team1 in xrange(N):
        total_games = 0
        won_games = 0
        for team2 in xrange(N):
            result = games.get((team1, team2), None)
            if result is not None:
                total_games += 1
                won_games += result
        wp[team1] = (won_games, total_games)
    return wp

def calc_owp(N, games, wp):
    owp = {}
    for team1 in xrange(N):
        team1_wp = wp[team1]
        owp_ = F()
        n_opponents = 0
        for team2 in xrange(N):
            if team1 == team2:
                continue
            team1_result = games.get((team1, team2), None)
            team2_wp = wp[team2]
            if team1_result is not None:
                n_opponents += 1
                if team1_result == 1:
                    team2_owp = F(team2_wp[0], 
                                  team2_wp[1] - 1)
                else:
                    assert team1_result == 0
                    team2_owp = F(team2_wp[0] - 1, 
                                  team2_wp[1] - 1)
                owp_ += team2_owp
        owp[team1] = owp_ / n_opponents
    return owp

def calc_oowp(N, games, owp):
    oowp = {}
    for team1 in xrange(N):
        oowp_ = F()
        n_opponents = 0
        for team2 in xrange(N):
            if team1 == team2:
                continue
            team1_result = games.get((team1, team2), None)
            if team1_result is not None:
                n_opponents += 1
                oowp_ += owp[team2]
        oowp[team1] = oowp_ / n_opponents
    return oowp

def solve(N, schedule):
    games = parse(N, schedule)
    wp = calc_wp(N, games)
    owp = calc_owp(N, games, wp)
    oowp = calc_oowp(N, games, owp)
    return [float(F(1, 4) * F(*wp[team]) +
                  F(1, 2) * owp[team] +
                  F(1, 4) * oowp[team])
            for team in xrange(N)]

if __name__ == '__main__':
    T = int(raw_input())
    for t in xrange(1, T + 1):
        N = int(raw_input())
        schedule = [raw_input() for _ in xrange(N)]
        rpi = solve(N, schedule)
        print 'Case #%d:' % t
        for f in rpi:
            print f
