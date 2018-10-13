##
# CODEJAM
# prillan91
##
import sys

def RPI(WP, OWP, OOWP):
    return 0.25 * WP + 0.50 * OWP + 0.25 * OOWP

def solveSingle(f):
    N = int(f.readline())
    
    s = []

    WPs = []
    OWPs = []
    OOWPs = []
    losses = []
    wins = []

    for i in xrange(N):
        s.insert(i, list(f.readline()))
        wins.insert(i, 0)
        losses.insert(i, 0)
        for x in s[i]:
            if x == '1':
                wins[i] += 1
            elif x == '0':
                losses[i] += 1
        WPs.insert(i, float(wins[i]) / (float(wins[i]) + float(losses[i])))
    #print WPs
    for i in xrange(N):
        bigsum = 0
        vs = 0
        for j in xrange(N):
            if not s[i][j] == '.':
                vs += 1
                bigsum += float(wins[j] - (1 if s[i][j] == '0' else 0)) / float(wins[j] + losses[j] - 1) 
        OWPs.insert(i, bigsum / vs)
    #print OWPs
    for i in xrange(N):
        bigsum = 0
        vs = 0
        for j in xrange(N):
            if not s[i][j] == '.':
                vs += 1
                bigsum += OWPs[j]
        OOWPs.insert(i, float(bigsum) / float(vs))
    #print OOWPs

    ret = "\n"

    for i in xrange(N):
        #print "TEAM " + str(i)
        rpi =  RPI(WPs[i], OWPs[i], OOWPs[i])
        #print rpi
        ret += str(rpi) + "\n"

    return ret
def solve():
    f = open(sys.argv[1])
    o = open(sys.argv[1] + ".out", 'w')
    T = int(f.readline())

    for t in range(T):
        print t + 1
        o.write("Case #" + str(t + 1) + ": " + str(solveSingle(f)))
        


solve()
