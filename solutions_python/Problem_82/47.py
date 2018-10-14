import sys
from fractions import gcd
cin = sys.stdin.readline

def cando(D, tups, canmove):
    #print "trying", canmove
    curr = -1e99
    for P, V in tups:
        #print P,V
        for i in xrange(V):
            if P+canmove < curr+D:
                #print "FAIL"
                return False
            curr = max(curr+D, P-canmove)
            #print P,V,curr
    return True
            
        

def solve(D, tups):
    low, high = 0.0, 1e10
    mid = 0.0
    for i in xrange(63):
        mid = (low + high) * 0.5
        if cando(D, tups, mid):
            high = mid
        else:
            low = mid
    return (low+high)*0.5
    
                                


if __name__ == '__main__':
    T = int(cin())
    for cnum in xrange(T):
        C, D = [int(i) for i in cin().strip().split()]
        tups = [tuple(int(t) for t in cin().strip().split()) for i in xrange(C)]
        print "Case #%d: %.12lf" % (cnum+1, solve(D, tups))
                    
            
        
    
