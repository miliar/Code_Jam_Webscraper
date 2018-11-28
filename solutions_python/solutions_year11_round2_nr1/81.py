from sys import argv
from itertools import izip, imap, count, combinations, permutations
import math

def rate01( row ):
    n0, n1 = 0, 0
    for i in row:
        if i == "0":
            n0 += 1
        elif i == "1":
            n1 += 1
    return float(n1)/(n0+n1)

def get_OWPd( results, n ):
    ret = [ [None for i in xrange(n)] for j in xrange(n) ]
    for ignore in xrange(n):
        for row in xrange(n):
            if ignore==row:
                owpd = 0
            else:
                owpd = rate01( results[row][:ignore] + results[row][ignore+1:] )
            ret[ignore][row] = owpd
    return ret

def get_OWP( results, OWPd, n ):
    ret = []
    for i in xrange(n):
        lst = []
        for j in xrange(n):
            if results[i][j] != ".":
                lst.append( OWPd[i][j] )
        ret.append( float(sum(lst)) / len(lst) )
    return ret

def get_OOWP( results, OWP, n ):
    ret = []
    for i in xrange(n):
        lst = []
        for j in xrange(n):
            if results[i][j] != ".":
                lst.append( OWP[j] )
        ret.append( float(sum(lst)) / len(lst) )
    return ret

def solvecase( nteams ):
    global inf
    results = [ [] for i in xrange(nteams) ]
    for i in xrange(nteams):
        r = inf.readline().strip()
        results[i] = [ j for j in r ]
    
    WP = [ rate01(i) for i in results ]
    #for i in WP:
    #    print i
        
    OWPd = get_OWPd( results, nteams )
    OWP = get_OWP( results, OWPd, nteams )
    OOWP = get_OOWP( results, OWP, nteams )
    return [  a/4 + b/2 + c/4 for a,b,c in izip( WP, OWP, OOWP ) ]

def main():
    global inf
    inf = argv[1]
    inf = open(argv[1])
    ncase = int(inf.readline().strip())
    for case in xrange(1, ncase+1):
        nteams = int(inf.readline().strip())
        ans = solvecase( nteams )
        print "Case #{n}:".format( n=case )
        for i in ans:
            print i

main()

