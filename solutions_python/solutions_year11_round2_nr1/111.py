T = int(raw_input())

for t in range(T):
    N = int(raw_input())
    plays = {}
    for n in range(N):
        for i,r in enumerate(raw_input()):
            if r == '1' or r == '0':
                plays.setdefault(n, {})[i] = int(r)

    wps = {}
    for i, m in plays.items():
        wps[i] = {}
        wins = float(sum(m.values()))
        matches = len(m)
        wps[i][i] = wins / matches
        
        for j,r in m.items():
            wps[i][j] = (wins - r) / (matches - 1)

    # Inverse index
    iwps = {}
    for i, m in wps.items():
        for j, r in m.items():
            iwps.setdefault(j, {})[i] = r

    # Calc OWP
    owps = {}
    for i in range(N):
        wp = wps[i][i]
        owps[i] = (sum(iwps[i].values()) - wp) / (len(iwps[i]) - 1)

    print "Case #%d:" % (t+1)
    for i in range(N):
        owp = owps[i]
        wp = wps[i][i]
        oowps = [owps[o] for o in wps[i] if o != i]
        oowp = sum(oowps) / len(oowps)


        rpi = wp * 0.25 + owp * 0.5 + oowp * 0.25
        print rpi
