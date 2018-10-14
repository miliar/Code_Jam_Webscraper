from sys import argv
from itertools import izip, imap, count, combinations, permutations, repeat, cycle
import math

def solvecase( L, t, N, C, a ):
    # from which point, booster possible?
    dist = [ j for i, j in izip(xrange(N), cycle( a )) ]
    
    eff = []
    accum = 0
    for d in dist:
        ori = d + d
        accum += ori
        if accum > t:
            r = min(accum - t, ori)
        else:
            r = 0
        eff.append( r )
    
    eff.sort(reverse=True)
    save = float( sum( eff[:L] ) ) / 2
    ans = accum - save
    if int(ans)==ans:
        return int(ans)
    return ans

def main():
    global inf
    inf = argv[1]
    inf = open(argv[1])
    ncase = int(inf.readline().strip())
    for case in xrange(1, ncase+1):
        #print "input", case
        line = inf.readline().strip()
        #print CD
        line = map(int, line.split())
        L, t, N, C = line[:4]
        a = line[4:]
        ans = solvecase( L, t, N, C, a )
        print "Case #{n}: {a}".format( n=case, a = ans )

main()
