#!/bin/env python2
import sys, math

def serving( r, q ):
    m = int( math.ceil( q/1.1/r ) )
    M = int( math.floor( q/0.9/r ) )
    for i in range(m-1, m+2):
        if i * r * 11 >= q * 10:
            break
    m = i
    for i in range(M+1, M-2, -1):
        #print "test M:", i
        if i * r * 9 <= q * 10:
            break
    M = i
    if m == 0: m = 1
    if M == None: return None
    return (m, M) if m <= M else None


def solve(N, P, R, Q):
    C = []
    for r, Qi in zip(R, Q):
        #print "Qi", Qi
        Ci = []
        for q in Qi:
            s = serving(r, q)
            #print "r, q, s", r, q, s
            if s:
                Ci.append(s)
        Ci.sort(reverse=True)
        C.append(Ci)
    #print "C", C
    k = 0
    while all(C):
        s, i = min( [ (Ci[-1], i) for i, Ci in enumerate(C) ] )
        #print "try C{0}: {1}".format(i, s)
        test = [ Ci[-1][0]<=s[1] for Ci in C ]
        #print test, C, [ (s, Ci[-1]) for Ci in C ]
        if all(test):
            k += 1
            #print "pop!"
            for Ci in C:
                Ci.pop()
        else:
            assert s == C[i].pop()
    return k

#solve( 1, 8, [10], [[11, 13, 17, 11, 16, 14, 12, 18]] )
#solve( 3, 3, [70,80,90], [[1260, 1500, 700],
#[800, 1440, 1600],
#[1700, 1620, 900]] )

def main():
    f = open( sys.argv[1] )
    T = int( f.next().strip() )
    for n in range(T):
        N, P = map(int, f.next().strip().split())
        R = map(int, f.next().strip().split())
        Q = [ map(int, f.next().strip().split()) for i in range(N) ]
        print "Case #{0}: {1}".format( n+1, solve(N, P, R, Q) )

main()


'''
100

990

10 serving

9 serving

11 serving
1100*0.9 = 990  

990 / 0.9 / 100 = 1100 / 100 = 11
990 / 1.1 / 100 = 900 / 100 = 9
'''
