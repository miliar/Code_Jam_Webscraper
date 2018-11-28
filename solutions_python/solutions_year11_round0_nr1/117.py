from sys import argv
from itertools import izip, imap, count, combinations, permutations

def solve_seq( seq ):
    tokenO, tokenB = 0, 0
    O, B = 1, 1
    totalcost = 0
    for s in seq:
        s, O, B, tokenO, tokenB
        if s[0] == "O":
            cost = abs( O - s[1] )
            O = s[1]
            if cost <= tokenO :
                realcost = 1
            else:
                realcost = 1 + cost - tokenO
            tokenB += realcost
            tokenO = 0
        else:
            cost = abs( B - s[1] )
            B = s[1]
            if cost <= tokenB :
                realcost = 1
            else:
                realcost = 1 + cost - tokenB
            tokenO += realcost
            tokenB = 0
        totalcost += realcost
    return totalcost

def line( l ):
    seq = l.split(" ")[1:]
    seq = zip(*([iter(seq)]*2))
    seq = [ (i[0], int(i[1])) for i in seq ]
    return solve_seq( seq )

def main():
    global inf, outf
    inf = argv[1]
    inf = open(argv[1])
    ncase = int(inf.readline().strip())
    for case in xrange(1, ncase+1):
        l = inf.readline().strip()
        ans = line( l )
        print "Case #{n}: {ans}".format(n=case, ans=ans)

main()


