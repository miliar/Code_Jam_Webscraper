f = open('A-large.in')
f_out = open('ProbA-large.out', 'w')
n = int(f.next())
test = 1
while test <= n:
    teams = int(f.next())
    results = []
    for line in xrange(teams):
        results.append(list(f.next().strip()))
    wps = []
    for r in results:
        won = 0
        games = 0
        for g in r:
            if g == '1':
                won += 1
                games += 1
            elif g == '0':
                games += 1
        wps.append(float(won)/float(games))
    owps = []
    for me in xrange(len(results)):
        wpsum = 0
        playedoppos = 0
        for oppos in xrange(len(results[me])):
            if oppos == me or results[me][oppos] == '.':
                continue
            playedoppos += 1
            oppos_won = 0
            oppos_games = 0
            for oppos_oppos in xrange(len(results[oppos])):
                if oppos_oppos == me or results[oppos][oppos_oppos] == '.':
                    continue
                oppos_games += 1
                if results[oppos][oppos_oppos] == '1':
                    oppos_won += 1
            wpsum += float(oppos_won)/float(oppos_games)
        owps.append(wpsum/float(playedoppos))
    oowps = []
    for me in xrange(len(results)):
        oowps_sum = 0
        oowps_amount = 0
        for oppos in xrange(len(results[me])):
            if results[me][oppos] == '.':
                continue
            oowps_amount += 1
            oowps_sum += owps[oppos]
        oowps.append(float(oowps_sum)/float(oowps_amount))
    f_out.write('Case #%d:\n' % (test,))
    for each in xrange(len(results)):
        rpi = 0.25 * wps[each] + 0.5 * owps[each] + 0.25 * oowps[each]
        f_out.write('%f\n' % (rpi,))
    test += 1
f.close()
f_out.close()
