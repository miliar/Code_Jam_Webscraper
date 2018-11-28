import psyco
psyco.full()

import sys, copy




def print_s(s):
    ps = []
    for ss in s:
        p = ss[0]
        o = ss[1]
        if p:
            p = 1
        else:
            p = 0
        if o:
            o = 1
        else:
            o = 0
        ps.append([p,o])
    print ps


def calc2(N,K):
    return (K+1) % (2**N) == 0

def calc(N,K):
    print "CASE:", N,K
    
    POW,ON = 0,1
    s = [[False,False] for a in xrange(N)] # bools: powered?, on?
    s[0][POW] = True
    
    print_s(s)
    
    for k in xrange(K):
        # snap effect
        for cs in s:
            if cs[POW]:
                cs[ON] = not cs[ON]
        # update powers
        for si in xrange(1,len(s)):
            ps,cs = s[si-1], s[si]
            cs[POW] = ps[POW] and ps[ON]
        
        print_s(s)
        
    
    ls = s[-1]
    if not ls[ON]==True or not ls[POW]:
        return False
    else:
        return True





def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cn = 1
for line in ig:
    N,K = [int(s) for s in line.split(' ')]
    v = calc2(N,K)
    if v:
        onoff = "ON"
    else:
        onoff = "OFF"
    print "Case #%d: %s" % (cn,onoff)
    cn += 1

