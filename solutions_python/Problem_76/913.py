#!/usr/bin/env python

import sys,getopt,itertools

# GCJ2011 Qualification Round
# solve Problem C.

def remain_pile(whole, p):
    w = list(whole)
    for x in p:
        if x in w: w.pop(w.index(x))
    return w

def solve(N, C, verbose=False):
    ans = 0
    if verbose: print >>sys.stderr, 'N:',N,'C:', C
    for n in xrange(1, N):
        for p in itertools.combinations(C, n):
            r = remain_pile(C, p)
            S_xs = reduce(lambda x,y:x^y, p)
            P_xs = reduce(lambda x,y:x^y, r)
            if verbose:
                print >>sys.stderr, 'Sean: ', p, '-> %d (xor %d)' % (sum(p), S_xs)
                print >>sys.stderr, 'Patt: ', r, '-> %d (xor %d)' % (sum(r), P_xs)
            if S_xs == P_xs:
                ans = max(ans, sum(p))

    if ans == 0: ans = 'NO'
    return ans

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hv', ['help', 'verbose'])
    except getopt.GetoptError, err:
        print str(err)
        print >>sys.stderr, sys.argv[0], '[-h] [-v]'
        sys.exit(2)
    verbose = False
    for o, a in opts:
        if o in ('-v', '--verbose'):
            verbose = True
        elif o in ('-h', '--help'):
            print >>sys.stderr, 'solve-A.py [-h] [-v]'
            sys.exit()
        else:
            assert False, 'unhandled option'
    
    line = sys.stdin.readline()
    T = int(line)
#main loop
#input handling
    if verbose:
        print >>sys.stderr, 'input %d test cases' % T
    for i in xrange(T):
        N = int(sys.stdin.readline())
        C = sys.stdin.readline().split()
        ans = solve(N, map(lambda x:int(x), C), verbose)
        print 'Case #%d:' % (i+1), ans

if __name__ == '__main__':
    main()

