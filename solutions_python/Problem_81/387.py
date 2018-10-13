import sys
from decimal import *

dt = Decimal

def hasplayed(tbl, a, b):
    if tbl[a][b] == '.':
        return False
    return True

def get_owp(tbl, team):
    t = dt(0)
    nplayed  = 0
    for i, r in enumerate(tbl):
        if i == team:
            continue
        if not hasplayed(tbl, i, team):
            continue
        nplayed += 1
        games = list(r)
        del games[team]
        games = ''.join(games)
        nwon = games.count('1')
        wp = dt(nwon)/(dt(len(games) - games.count('.')))
        t += wp
    return t/dt(nplayed)

def get_oowp(tbl, owps, team):
    t = dt(0)
    n = 0
    for i, owp in enumerate(owps):
        if hasplayed(tbl, i, team):
            t += owp
            n += 1
    return t/dt(n)

def solve(tbl, casen):
    owps = []
    rpis = []
    for i, t in enumerate(tbl):
        owps.append(get_owp(tbl, i))
    for team in xrange(len(tbl)):
        ngames = dt(len(tbl[team]) - tbl[team].count('.'))
        nwon = dt(tbl[team].count('1'))
        wp = nwon/ngames
        owp = owps[team]
        oowp = get_oowp(tbl, owps, team)
        # 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
        rpi = dt(0.25)*wp + dt(0.5)*owp + dt(0.25)*oowp
        rpis.append(rpi)
    print "Case #%d:" % casen
    for rpi in rpis:
        print float(rpi)

if __name__ == '__main__':
    with open(sys.argv[1], 'rU') as f:
        lines = f.readlines()
        ncases = int(lines[0])
        lines = lines[1:]
        for i in xrange(ncases):
            tbl = []
            nteams = int(lines[0])
            lines = lines[1:]
            for j in xrange(nteams):
                tbl.append(lines[j].strip())
            lines = lines[nteams:]
            solve(tbl, i+1)
