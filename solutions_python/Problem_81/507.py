fp = open('A-large.in')
T = int(fp.readline())

for t in range(T):
    N = int(fp.readline())
    M = []
    for n in range(N):
        s = fp.readline().strip()
        M.append(s)

    print "Case #%d:"%(t+1)

    WP = []
    for n in range(N):
        playcount = 0
        wins = 0.0
        wp = 0.0
        for i in range(len(M[n])):
            if M[n][i] == '0' :
                playcount += 1
            if M[n][i] == '1' :
                playcount += 1
                wins += 1
        if playcount != 0: wp = wins/playcount
        # print playcount, wins, (wins/playcount)
        WP.append(wp)

    OWP = []
    for n in range(N):
        owp = 0.0
        wpcount = 0.0
        for j in range(N):
            if M[j][n] != '.':
                playcount = 0
                wins = 0.0
                wp = 0.0
                for i in range(len(M[n])):
                    if (M[j][i] == '0') and (i != n):
                         playcount += 1
                    if (M[j][i] == '1') and (i != n):
                         playcount += 1
                         wins += 1
                if playcount != 0:
                    wp = wins/playcount
                    wpcount +=1
                    owp += wp
        OWP.append(owp/wpcount)

    OOWP = []
    for n in range(N):
        oowp = 0.0
        count = 0.0
        for i in range(N):
            if M[n][i] != '.':
                oowp += OWP[i]
                count += 1
        OOWP.append(oowp/count)

    for n in range(N):
        RPI = 0.25 * WP[n] + 0.50 * OWP[n] + 0.25 * OOWP[n]
        print RPI


