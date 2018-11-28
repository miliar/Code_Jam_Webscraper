from itertools import *

infile = "A-small-attempt0.in"

lines = [s.rstrip() for s in open(infile, "rb").readlines()]
NCases=int(lines[0])


def WP (matches, ti, exclude=[]):
    nloss = len( [m for j,m in enumerate(matches[ti]) if m == '0' and j not in exclude])
    nwin = len( [m for j,m in enumerate(matches[ti]) if m == '1' and j not in exclude])
    return ((nwin * 1.0) / (nwin + nloss))

def OWP (matches, ti):
    wps = []
    for j,m in enumerate(matches[ti]):
        if (m != '.'):
            wps.append(WP (matches, j, exclude=[ti]))
    return (sum(wps) / len(wps))

def OOWP (matches, ti):
    owps = []
    for j,m in enumerate(matches[ti]):
        if (m != '.'):
            owps.append(OWP(matches, j))
    return (sum(owps) / len(owps))
    
def RPI (matches, ti):
    return (0.25 * WP (matches, ti) + 
            0.5 * OWP (matches, ti) + 
            0.25 * OOWP (matches, ti))


pos = 1
for i in range(NCases):
    Nteams = int(lines[pos])
    matches = []
    for ti in range(Nteams):
        matches_ti = []
        scores = lines[pos + ti + 1]
        for tj, sc in enumerate(scores):
            matches_ti.append(sc)
        matches.append(matches_ti)
                    
    pos += Nteams + 1
    print "Case #%d:" % (i+1)
    for ti in range(Nteams):
        print RPI (matches, ti)