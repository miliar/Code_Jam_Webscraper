t = input()
for i in range(t):
    c = []
    winner = 'm'
    for a in range(4):
        c.append(raw_input())
    raw_input()
    for a in c:
        fl = a[0]
        if (fl == 'T'):
            fl = a[1]
        for b in a:
            if (b != fl and b != 'T'):
                fl = 'm'
        if (fl != 'm' and fl != '.'):
            winner = fl
    for a in range(len(c[0])):
        fl = c[0][a]
        if (fl == 'T'):
            fl = c[1][a]
        for b in range(len(c)):
            if (c[b][a] != fl and c[b][a] != 'T'):
                fl = 'm'
        if (fl != 'm' and fl != '.'):
            winner = fl
    fl = c[0][0]
    if (fl == 'T'):
        fl = c[1][1]
    for b in range(len(c)):
        if (c[b][b] != fl and b != 'T'):
            fl = 'm'
    if (fl != 'm' and fl != '.'):
        winner = fl
    fl = c[0][len(c) - 1]
    if (fl == 'T'):
        fl = c[1][len(c) - 2]
    for b in range(len(c)):
        if (c[b][len(c) - b - 1] != fl and c[b][len(c) - b - 1] != 'T'):
            fl = 'm'
    if (fl != 'm' and fl != '.'):
        winner = fl
    if (winner != 'm'):
        print "Case #%d: %c won" % (i + 1, winner)
    else:
        fl = True
        for a in c:
            for b in a:
                if (b == '.'):
                    fl = False
        if (fl):
            print "Case #%d: Draw" % (i + 1)
        else:
            print "Case #%d: Game has not completed" % (i + 1)
