cases = raw_input()
for case in xrange(int(cases)):
    t = int(raw_input())
    sc = []
    for i in xrange(t):
        sc.append([j for j in raw_input()])

    owp = []
    for i in xrange(t):
        p = []
        for j in xrange(t):
            if sc[i][j] != '.':
                p.append(j)
        _owp = 0   
        for j in p:
            owin, oplay = 0.0, 0.0
            play = len(p)
            for k in xrange(t):
                if k != i and sc[j][k] != '.':
                    oplay += 1
                    if sc[j][k] == '1':
                        owin +=1
            _owp += owin / oplay / play

        owp.append(_owp)

    output = ''
    for i in xrange(t):
        wp, oowp, win, play = 0.0, 0.0, 0.0, 0.0
        for j in xrange(t):
            if sc[i][j] != '.':
                oowp += owp[j]
                play += 1
                if sc[i][j] == '1':
                    win += 1
        wp = win / play
        oowp = oowp / play
        rpi = 0.25 * wp + 0.5 * owp[i] + 0.25 * oowp
        output += '\n' + str(rpi)
            
    print 'Case #%d:%s' % (case + 1, output)
