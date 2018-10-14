# crop.py

import sys

def main(inputfile):
    f = open(inputfile)
    ncases = int(f.next())
    for i,line in enumerate(f):
        print 'Case #%d: %d' % (i+1, solve(*map(int, line.strip().split())))

def solve(A, B, P):
    primes = primes_up_to(B)
    def merge_p(a,b):
        # return true if a and b share a prime factor >= P
        for p in primes:
            if p<P:
                continue
            if a%p == 0 and b%p == 0:
                return True
        return False
            
    d = {}
    N = B-A+1
    for i in xrange(A, B+1):
        d[i] = set((i,))
    for a in xrange(A, B+1):
        for b in xrange(a+1, B+1):
            if d[a] is not d[b] and merge_p(a,b):
                newset = d[a] | d[b]
                for v in newset:
                    d[v] = newset
                N -= 1
    assert N == len(set(id(s) for s in d.itervalues()))
    return N

        
def primes_up_to(M):
    P = [2,3,5,7,11,13,17,19]
    for i in xrange(23, M+1, 2):
        for p in P:
            if i%p==0:
                break
            if p*p > i:
                P.append(i)
                break
        else:
            P.append(i)
    return P


if __name__ =='__main__':
    #default = 'B-sample.in'
    default = 'B-small-attempt4.in'
    f = sys.argv[1] if len(sys.argv)>1 else default
    main(f)
