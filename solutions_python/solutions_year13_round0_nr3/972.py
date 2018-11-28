import sys
from math import sqrt

def is_fair(nr):
    snr = str(nr)
    l = len(snr)/2
    for _l in xrange(l):
        if snr[_l] != snr[-_l-1]:
            return False
    return True

def is_fairsquare(nr):
    if not is_fair(nr):
        return False
    
    sq = sqrt(nr)
    if not sq.is_integer():
        return False
    sq = int(sq)
    if not is_fair(sq):
        return False
    return True

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        interv = [int(c) for c in f.readline().rstrip().split(' ')]
        cnt = 0
        for _i in xrange(interv[0], interv[1]+1):
            if is_fairsquare(_i):
                cnt += 1
        # print 
        # lawn = []
        # for _n in xrange(n):
        #     lawn.append( [int(p) for p in f.readline().split()] ) 
        
        # res = patternpossible(lawn, n, m)
        print "Case #%d: %d" % (_t+1, cnt)

