ifile = open('a-large.in','r')
ofile = open('a-large.out','w')

cases = int(ifile.readline().rstrip('\n'))
for c in xrange(1,cases+1):
    teams = int(ifile.readline().rstrip('\n'))
    scores = []
    for x in xrange(0,teams):
        scores.append([])
        scorestr = ifile.readline().rstrip('\n')
        for y in xrange(0,teams):
            scores[x].append(0)
            if scorestr[y] == '1':
                scores[x][y] = 1
            if scorestr[y] == '0':
                scores[x][y] = -1
    # print scores
    wp = []
    for x in scores:
        wins = 0.0
        matches = 0.0
        for y in x:
            if y:
                matches += 1.0
                if y == 1:
                    wins += 1.0
        wp.append((wins,matches))
    newwp = []
    for x in xrange(0,teams):
        newwp.append([])
        for y in xrange(0,teams):
            if scores[x][y] == 0:
                newwp[x].append(-1)
            elif scores[x][y] == 1:
                newwp[x].append((wp[x][0] - 1.0) / (wp[x][1] - 1.0))
            else:
                newwp[x].append(wp[x][0] / (wp[x][1] - 1.0))
    owp = []
    for x in xrange(0,teams):
        matches = 0.0
        wps = 0.0
        for y in xrange(0,teams):
            if scores[x][y]:
                matches += 1.0
                wps += newwp[y][x]
        owp.append(wps / matches)
    # print owp
    oowp = []
    for x in xrange(0,teams):
        matches = 0.0
        owps = 0.0
        for y in xrange(0,teams):
            if scores[x][y]:
                matches += 1.0
                owps += owp[y]
        oowp.append(owps / matches)

    ofile.write('Case #' + str(c) + ':\n')
    for x in xrange(0,teams):
        ofile.write(str(0.25 * (wp[x][0] / wp[x][1]) + 0.5 * owp[x] + 0.25 * oowp[x]))
        ofile.write('\n')

ifile.close()
ofile.close()
