import psyco
psyco.full()
import sys




def calc(games):
    wp = {} # WP for all teams in form (wins,total)
    for ti,res in games.items():
        wp[ti] = (res.values().count(1),len(res))
    owp = {} # OWP for all teams
    for ti in xrange(len(games)):
        swp = 0
        for oti in games[ti].keys():
            ow,ot = wp[oti]
            mow = ow-games[oti][ti]
            mot = ot-1
            op = mow/float(mot)
            swp += op
        cnt = len(games[ti].keys())
        owp[ti] = swp/float(cnt)
    oowp = {} # OOWP for all teams
    for ti in xrange(len(games)):
        sowp = 0
        for oti in games[ti].keys():
            sowp += owp[oti]
        cnt = len(games[ti].keys())
        oowp[ti] = sowp/float(cnt)
    ret = []
    for ti in xrange(len(games)):
        WP = wp[ti][0]/float(wp[ti][1])
        OWP = owp[ti]
        OOWP = oowp[ti]
        rpi = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
        ret.append(rpi)
        
#    #debug
#    if len(games)==4:
#        def test(name,actual,expected):
#            if actual!=expected:
#                print "FAIL:", name, "actual", actual, "expected", expected
#        print games
#        test("OOWP A", oowp[0], 7/12.)
#        test("OWP A", owp[0], 0.5)
#        test("OWP B", owp[1], 0.5)
#        test("OWP C", owp[2], 2/3.)
#        test("OWP D", owp[3], 0.25)
#        test("WP A", wp[0], (2,2))
#        test("WP B", wp[1], (0,3))
#        test("WP C", wp[2], (2,3))
#        test("WP D", wp[3], (1,2))
#        
#        print "OOWP A,B,C,D", oowp[0],oowp[1], oowp[2], oowp[3]
#        print "OWP A,B,C,D", owp[0],owp[1], owp[2], owp[3]
#        print "WP A,B,C,D", wp[0],wp[1], wp[2], wp[3]
#        print "A RPI", ret[0]
#        print """
#        WP
#          A has WP = 1, 
#          B has WP = 0, 
#          C has WP = 2/3, 
#          D has WP = 0.5.
#        
#        OWP team D: (B has WP = 0, C has WP = 0.5.) 
#          D has OWP = 0.5 * (0 + 0.5) = 0.25. 
#          A has OWP = 0.5, 
#          B has OWP = 0.5, 
#          C has OWP = 2/3.
#          
#        OOWP    
#          A has OOWP = 0.5 * (0.5 + 2/3) = 7/12. 
#    
#        RPI
#           A has RPI = (0.25 * 1) + (0.5 * 0.5) + (0.25 * 7 / 12) = 0.6458333...         
#        """
#        
    return ret

def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cn = 1
for line in ig:
    games = {} # tid --> {opptid --> result}
    for ti in xrange(int(line)):
        tline = ig.next()
        games[ti] = {}
        for oi,c in enumerate(tline):
            if c != '.':
                games[ti][oi] = int(c)
    
    v = calc(games)
    print "Case #%d:" % (cn,)
    for vv in v:
        s = "%.12f" % (vv,)
        print s.rstrip('0')
    cn += 1
