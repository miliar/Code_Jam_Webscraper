#!/usr/bin/python

T = input()
for case in xrange(1,T+1):
    n = input()
    sch = []
    for i in xrange(n):
        s = raw_input()
        sch.append(s)
    wp = []
    owp = []
    oowp = []
    for i,s in enumerate(sch):
        played = 0
        won = 0
        awp = []
        for j,c in enumerate(s):
            if c == '1':
                won += 1
            if c != '.':
                played += 1
                played1 = 0
                won1 = 0
                for j1,c1 in enumerate(sch[j]):
                    if j1 == i:
                        continue
                    if c1 != '.':
                        played1 += 1
                    if c1 == '1':
                        won1 += 1
                awp.append(won1/(played1+0.0))
        wp.append(won/(played+0.0))
        owp.append(sum(awp)/(len(awp)+0.0))
    all_owp = sum(owp)

    rpi = []
    for i,s in enumerate(sch):
        sum_owp = 0
        count_owp = 0
        for j,c in enumerate(s):
            if c != '.':
                sum_owp += owp[j]
                count_owp += 1
        oowp.append(sum_owp/(count_owp+0.0))
        rpi.append(0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i])

    print "Case #%d:"%case
    for r in rpi:
        print r

