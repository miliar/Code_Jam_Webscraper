from __future__ import division

def rins():
    return raw_input().strip()


def calc_wins(resultline):
    return sum(1.0 for r in resultline if r=="1")
def calc_games(resultline):
    return sum(1.0 for r in resultline if r!=".")
def game_happened(a,b,matches):
    return matches[a][b]!="."
def first_team_won(a,b,matches):
    return matches[a][b]=="1"

def solve_next():
    n = int(rins())
    match_results = [rins() for i in xrange(n)]
    wins = [calc_wins(resultline) for resultline in match_results]
    played = [calc_games(resultline) for resultline in match_results]
    owp = []
    for team_a in xrange(n):
        opp_wp = 0
        opp_count = 0
        for team_b in xrange(n):
            if team_b == team_a:
                continue
            if game_happened(team_a, team_b, match_results):
                opp_wins = wins[team_b] if first_team_won(team_a, team_b, match_results) else wins[team_b] - 1
                opp_games = played[team_b] - 1
                opp_count += 1
                opp_wp += opp_wins / opp_games
            #else:
            #    opp_wins = wins[team_b]
            #    opp_games = played[team_b]
        owp.append(opp_wp / opp_count)
    oowp = []
    for team_a in xrange(n):
        opp_owp = 0
        opp_count = 0
        for team_b in xrange(n):
            if team_b == team_a:
                continue
            if game_happened(team_a, team_b, match_results):
                opp_count += 1
                opp_owp += owp[team_b]
        oowp.append(opp_owp / opp_count)
    for team in xrange(n):
        yield 0.25 * (wins[team]/played[team]) + 0.5 * owp[team] + 0.25 * oowp[team]

def run():
    t = int(rins())
    for i in xrange(t):
        print "Case #{0}:".format(i+1)
        for v in solve_next():
            print v

run()
