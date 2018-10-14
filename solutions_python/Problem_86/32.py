from sys import argv
from itertools import izip, imap, count, combinations, permutations
import math

def solvecase( freq, L, H ):
    for x in xrange(L, H+1):
        ok = True
        for f in freq:
            if f <= x :
                if (x % f) == 0:
                    continue
            else :
                if (f % x) == 0:
                    continue
            ok = False
            break
        if ok:
            return x
    return "NO"

def main():
    global inf
    inf = argv[1]
    inf = open(argv[1])
    ncase = int(inf.readline().strip())
    for case in xrange(1, ncase+1):
        #print "input", case
        NLH = inf.readline().strip()
        #print CD
        N, L, H = map(int, NLH.split())
        freq = inf.readline().strip()
        freq = map(int, freq.split())
        ans = solvecase( freq, L, H )
        print "Case #{n}: {a}".format( n=case, a = ans )

main()
