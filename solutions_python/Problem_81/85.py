import sys

t = int(sys.stdin.readline())

case = 1

while True:
    line = sys.stdin.readline()
    line = line.rstrip()
    if len(line) == 0:
        break

    print("Case #{}:".format(case))
    n = int(line)
    teams = []
    for i in range(n):
        line = sys.stdin.readline()
        line = line.rstrip()
        teams.append(line)

    wins = []
    games = []
    for team in teams:
        w = 0
        g = 0
        for x in team:
            if x == '1':
                w += 1
                g += 1
            elif x == '0':
                g += 1
        wins.append(w)
        games.append(g)

    wp = []
    owp = []
    for i in range(len(teams)):
        wpi = 0
        wpi += 0.25*wins[i]/games[i]
        owpsum = 0
        ocount = 0
        for j in range(len(teams[i])):
            if teams[i][j] == '1':
                ow = wins[j]
                og = games[j]-1
                owpsum += float(ow)/og
                ocount += 1
            if teams[i][j] == '0':
                ow = wins[j]-1
                og = games[j]-1
                owpsum += float(ow)/og
                ocount += 1
        wp.append(wins[i]/games[i])
        owp.append(owpsum/ocount)

    for i in range(len(teams)):
        wpi = 0
        wpi += 0.25*wins[i]/games[i]
        wpi += 0.5*owp[i]
        owpsum = 0
        ocount = 0
        for j in range(len(teams[i])):
            if teams[i][j] != '.':
                owpsum += owp[j]
                ocount += 1
        wpi += 0.25*(float(owpsum)/ocount)

        print(wpi)

    case += 1
