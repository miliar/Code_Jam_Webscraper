import sys


knowledge_base = {}

def main():
    infile = open(sys.argv[1]) if len(sys.argv)>1 else sys.stdin
    T = int(next(infile))
    for case_no in xrange(1, T+1):
        N, K = map(int, next(infile).split(' '))
        ret = solve(N, K)
        print 'Case #%d: %s %s' % (case_no, ret[0], ret[1])
   
def solve (n,k):
    
    if (n, k) in knowledge_base:
        return knowledge_base[(n, k)]
    
    if k==n:
        ret = (0,0)
    elif k==0:
        ret = (n,n)
    elif k==1:
        if n&1:
            ret = ((n-1)/2,(n-1)/2)
        else:
            ret = (n/2, n/2-1)
    elif n&1 and k&1:
        #odd, odd
        ret = solve((n-1)/2, (k-1)/2)
    elif n&1 and not k&1:
        #odd, even
        m1,m2 = solve((n-1)/2, k/2)
        m3,m4 = solve((n-1)/2, k/2-1)
        ret = (min(m1,m3), min(m2,m4))
    elif not n&1 and k&1:
        #even, odd
        m1,m2 = solve(n/2, (k-1)/2)
        m3,m4 = solve(n/2-1, (k-1)/2)
        ret = (min(m1,m3), min(m2,m4))
    else:
        # even, even
        m1,m2 = solve(n/2, k/2)
        m3,m4 = solve(n/2-1, k/2)
        m5,m6 = solve(n/2, k/2-1)
        m7,m8 = solve(n/2-1, k/2-1)
        
        p1,p2 = min(m1,m7), min(m2,m8)
        p3,p4 = min(m3,m5), min(m4,m6)
        
        ret = (max(p1,p3), max(p2,p4))
        
    knowledge_base[(n,k)] = ret
    return ret
    


if __name__ == '__main__':
    main()
