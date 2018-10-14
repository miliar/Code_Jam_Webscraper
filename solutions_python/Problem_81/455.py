#!/usr/bin/env python

import sys

def line():
    return sys.stdin.readline().strip()

def readint():
    return int(line())

def intline():
    return map(int, line())

def compute_owp(teams, wplist):
    owplist = []
    for ixout,(w,l) in enumerate(teams):
        tot = 0.0
        opponents = w.union(l)
        for ix in opponents:
            ow,ol = teams[ix]
            ngames = len(ow) + len(ol)
            num = 1.0 if ixout in ow else 0.0
            wp_old = wplist[ix]*float(ngames)
            wp_old -= num
            tot += wp_old/float(ngames - 1)
        owplist.append(float(tot)/float(len(opponents)))
    return owplist

def compute_oowp(teams, owplist):
    oowplist = []
    for ixout,(w,l) in enumerate(teams):
        tot = 0.0
        opponents = w.union(l)
        for ix in opponents:
            tot += owplist[ix]
        oowplist.append(float(tot)/float(len(opponents)))
    return oowplist

def main(argv):
    t = readint()
    for caseno in xrange(t):
        n = readint()
        teams = []
        for rowix in xrange(n):
            teamw = set()
            teaml = set()
            row = line()
            for colix,c in enumerate(row):
                if c == '1':
                    teamw.add(colix)
                elif c == '0':
                    teaml.add(colix)
                else:
                    assert c == '.'
            teams.append((teamw,teaml))
        wplist = []
        for ix,(w,l) in enumerate(teams):
            tot = len(w) + len(l)
            wplist.append(float(len(w))/float(tot))
        owplist = compute_owp(teams, wplist)
        oowplist = compute_oowp(teams, owplist)
        print "Case #%d:" % (caseno + 1)
        for ix in xrange(len(teams)):
            print 0.25*wplist[ix] + 0.5*owplist[ix] + 0.25*oowplist[ix]
        
            

if __name__ == "__main__":
    sys.exit(main(sys.argv))
