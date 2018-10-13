infile = open('rpi.in')
outfile = open('rpi.out', 'w')

T = int(infile.readline().strip())

for t in xrange(T):
    outfile.write('Case #%d:\n' % (t + 1))
    N = int(infile.readline().strip())

    matchups = [infile.readline().strip() for i in xrange(N)]
    win_loss_counts = [(m.count('1'), m.count('0')) for m in matchups]

    opp_counts = [wl[0] + wl[1] for wl in win_loss_counts]
    wp = [wl[0] / float(wl[0] + wl[1]) for wl in win_loss_counts]

    opp_wp = []
    for i in xrange(N):
        wp_sum = 0.0
        for j in xrange(N):
            if matchups[i][j] == '.': continue
            wins, losses = win_loss_counts[j]
            if matchups[i][j] == '1':
                losses -= 1
            else:
                wins -= 1
            wp_sum += wins / float(wins + losses)
        opp_wp.append(wp_sum / opp_counts[i])

    opp_opp_wp = []
    for i in xrange(N):
        opp_opp_wp.append(sum(opp_wp[j] for j in xrange(N)
                              if matchups[i][j] != '.') / opp_counts[i])

    for i in xrange(N):
        rpi = 0.25 * wp[i] + 0.5 * opp_wp[i] + 0.25 * opp_opp_wp[i]
        outfile.write('%0.12f\n' % rpi)
    

    pass
