for case in xrange(input()):
    n = input()
    d = [raw_input() for i in xrange(n)]
    scores = [[float(c) for c in l if c != '.'] for l in d]
    d2 = [[[float(c) for j, c in enumerate(l) if j!=i and c!='.'] for l in d] for i in xrange(n)]
    wp = [sum(s)/len(s) for s in scores]
    wp2 = [[sum(l)/len(l) for l in m] for m in d2]
    played = [[char!='.' and 1 or 0 for char in line] for line in d]
    owp = [sum([p[0]*p[1] for p in zip(wp2[i],t)])/sum(t) for i, t in enumerate(played)]
    oowp = [sum([p[0]*p[1] for p in zip(owp,t)])/sum(t) for t in played]
    rpi = [.25*t[0] + .5*t[1] + .25*t[2] for t in zip(wp, owp, oowp)]
    print "Case #%d:" % (case+1)
    print'\n'.join(map(str, rpi))
