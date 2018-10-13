#!/usr/bin/python

n = int(raw_input(''))
games = []

for _ in range(n):

    game = []

    for _ in range(4):
        game.append(list(raw_input('')))

    games.append(game)
    raw_input()

size = 4

case = 0
for game in games:
    case += 1
    incomplete = False
    hasResult = False

    for i in range(size):
        d = {'.': False, 'X': False, 'O': False}
        for j in range(size):
            d[game[i][j]] = True

        if d['.']:
            incomplete = True
            continue

        if d['X'] and d['O']:
            continue

        if d['X']:
            print "Case #%d: %s won" % (case, 'X')
            hasResult = True
            break

        if d['O']:
            print "Case #%d: %s won" % (case, 'O')
            hasResult = True
            break

        else:
            continue
        break

    if hasResult:
        continue

    for i in range(size):
        d = {'.': False, 'X': False, 'O': False}
        for j in range(size):
            d[game[j][i]] = True

        if d['.']:
            incomplete = True
            continue

        if d['X'] and d['O']:
            continue

        if d['X']:
            print "Case #%d: %s won" % (case, 'X')
            hasResult = True
            break

        if d['O']:
            print "Case #%d: %s won" % (case, 'O')
            hasResult = True
            break

        else:
            continue
        break

    if hasResult:
        continue

    for i in range(2):
        d = {'.': False, 'X': False, 'O': False}
        for j in range(size):
            if i == 0:
                d[game[j][j]] = True
            else:
                d[game[j][size-j-1]] = True

        if d['.']:
            incomplete = True
            continue

        if d['X'] and d['O']:
            continue

        if d['X']:
            print "Case #%d: %s won" % (case, 'X')
            hasResult = True
            break

        if d['O']:
            print "Case #%d: %s won" % (case, 'O')
            hasResult = True
            break

        else:
            continue
        break

    if hasResult:
        continue

    if incomplete:
        print "Case #%d: Game has not completed" % case
        continue

    print "Case #%d: Draw" % case
