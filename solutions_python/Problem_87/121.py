from sys import argv
from itertools import izip, imap, count, combinations, permutations
import math
from operator import itemgetter

def solvecase( X, S, R, t, N, lanes ):
    lanes = [ (i[2], i[1]-i[0]) for i in lanes ]
    lanes.sort()
    left = X - sum( map( itemgetter(1), lanes ) )
    
    #print "left", left
    
    T = 0
    c = min( left / R, t )
    T += c
    t -= c
    if t > 0:  # all run
        #print "left used", c, t
        i = 0
        for w, l in lanes:
            c = min( l / (R+w), t )
            T += c
            t -= c
            if t <= 0:
                T += ( l - c * (R+w) ) / (S+w)
                i += 1
                break
            else:
                #print "l used", l, c, t, R+w, S+w, T
                i += 1
                if i == len(lanes):
                    break
    else :
        #print "left used", c + ( left - c * R ) / S, t
        i = 0
        T += ( left - c * R ) / S 
    
    #print i, len(lanes)
    T += sum( [ l / (S+w) for w, l in lanes[i:] ] )
    
    return T

def main():
    global inf
    inf = argv[1]
    inf = open(argv[1])
    ncase = int(inf.readline().strip())
    for case in xrange(1, ncase+1):
        #print "input", case
        XSRtN = inf.readline().strip()
        #print CD
        X, S, R, t, N = map(float, XSRtN.split())
        N = int(N)
        lanes = []
        for i in xrange(N):
            BEw = inf.readline().strip()
            #print PV
            B, E, w = map(float, BEw.split())
            lanes.append( (B, E, w) )
        #lanes.sort()
        ans = solvecase( X, S, R, t, N, lanes )
        print "Case #{n}: {a}".format( n=case, a = ans )

main()
