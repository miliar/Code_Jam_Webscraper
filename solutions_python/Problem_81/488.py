from __future__ import division

def _WP(team, sch, N, exclude=None):
        s = sch[team]
        Wins = Losses = 0
        O = []
        for x in xrange(N):
            if (exclude != None and exclude == x):
                continue
                
            if s[x] == '1':
                Wins += 1
                O.append(x)
            elif s[x] == '0':
                Losses += 1
                O.append(x)
        return (Wins / (Wins+Losses), O)
        
def _OWP(team, sch, N):
    O = _WP(team, sch, N)[1]
    OWP, Oc = 0, len(O)
    if (not O): return OWP
    
    for o in O:
        OWP += _WP(o, sch, N, team)[0]
    return OWP / Oc

def run(_):
    print "Case #%d:" % _
    N    = int(raw_input())
    WP   = []
    OWP  = []
    OOWP = []
    O    = []
    sch  = []
    for n in xrange(N):
        sch.append(list(raw_input()))
        
    for n in xrange(N):
        i, k = _WP(n, sch, N)
        WP.append(i)
        O.append(k)
        OWP.append(_OWP(n, sch, N))
        
    for n in xrange(N):
        Oc = len(O[n])
        if (Oc):
            OOWP.append(sum([OWP[x] for x in O[n]]) / Oc)
        else:
            OWP.append(0)
    
    for n in xrange(N):
        # RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
        print ((0.25 * WP[n]) + (0.50 * OWP[n]) + (0.25 * OOWP[n]))

    

T = int(raw_input())
for _ in xrange(1, T+1) :
    run(_)