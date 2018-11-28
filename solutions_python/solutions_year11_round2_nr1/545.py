#!/usr/bin/python3


def WP(results, team, exclude=None):
    wins = 0
    games = 0
    for i, game in enumerate(results[team]):
        if game == '1' and i != exclude:
            wins += 1
        if game == '.' or i == exclude:
            continue
        games += 1
    return wins/games


def OWP(results, team):
    summ = 0
    q = 0
    for i, game in enumerate(results[team]):
        if game != '.':
            summ += WP(results, i, team)
            q += 1
    return summ/q

def OOWP(results, team):
    summ = 0
    q = 0
    for i, game in enumerate(results[team]):
        if game != '.':
            summ += OWP(results, i)
            q += 1
    return summ/q

def main():
    t = int(input())
    for i in range(t):
        teams = int(input())
        results = []
        for j in range(teams):
            results.append(list(input()))
        wp = []
        for team in range(len(results)):
            wp.append(WP(results, team))
        owp = []
        for team in range(len(results)):
            owp.append(OWP(results, team))
        oowp = []
        for team in range(len(results)):
            oowp.append(OOWP(results, team))
        print("Case #{0}:".format(i+1))
        for team in range(len(results)):
            print(0.25*wp[team] + 0.50*owp[team] + 0.25*oowp[team])

if __name__ == '__main__':
    main()
