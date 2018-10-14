import sys
import numpy as n


f = open(sys.argv[1], 'r')
lines = f.readlines()[1:]
nn = 0
last = 0
for i,l in enumerate(lines):
    l = l.strip()
    if len(l) == 1 or i == 0 or i == last:
        nn += 1
        teams = int(l)
        wins = n.zeros((teams,teams))
        last = i + teams + 1
        for ii in range(i+1,i+teams+1):
            for jj,c in enumerate(lines[ii].strip()):
                if c == '1':
                    s = 1
                if c == '0':
                    s = -1
                if c == '.':
                    s = 0
                wins[ii-i-1][jj] = s
        WPS = n.zeros(teams)

        for i in range(teams):
            win, loss = 0, 0
            for j in range(teams):
                if wins[i][j] == 1:
                    win += 1
                if wins[i][j] == -1:
                    loss += 1
            WP = float(win)/float(win + loss)
            WPS[i] = WP
       # print wins
        #print WPS
        OWPS = n.zeros((teams,teams))

        for i in range(teams): # i OWP
            for j in range(teams): # i oppoenents
                if i != j:
                    win, loss = 0, 0
                    count = 0
                    OWP = 0.0
                    for k in range(teams): # j's games
                        if k != i and k != j: # discard games against i

                            if wins[j][k] == 1:
                                win += 1
                            if wins[j][k] == -1:
                                loss += 1
                    if win+loss > 0:
                        WP = float(win)/float(win + loss)
                        OWP += WP
                        count += 1
                        OWPS[i][j] = OWP/count
                    else:
                        WP = 0

        #print OWPS, "owps"

        nOWPS = n.zeros(teams)
        for i in range(teams):
            count = 0
            s = 0.0
            for j in range(teams):
                if i != j and wins[i][j] != 0:
                    s += OWPS[i][j]
                    count += 1
            nOWPS[i] = s/count

        OWPS = nOWPS
        #print OWPS

        OOWP = n.zeros(teams)
        for i in range(teams):
            oowp = 0.0
            count = 0
            for j in range(teams):
                if wins[i][j] != 0:
                    oowp += OWPS[j]
                    count += 1
            if count > 0:
                OOWP[i] = oowp/count

        #print OOWP

        print "Case #%s:" % str(nn)
        for i in range(teams):
            print 0.25 * WPS[i] + 0.50 * OWPS[i] + 0.25 * OOWP[i]