################################################################
def solve():
    (P,) = [int(x) for x in input.readline().split(' ')]
    M = [int(x) for x in input.readline().split(' ')]
    PRICES = [[int(x) for x in input.readline().split(' ')] for i in range(0,P)]
    def cost(M,PRICES):
        if len(M) == 1:
            if M[0] < 0: return 999999999999999
            else: return 0
        last = PRICES[-1:][0][0]
        nix = PRICES[:-1]
        P1 = [l[0:len(l)/2] for l in nix]
        P2 = [l[len(l)/2:] for l in nix]
        M1 = M[0:len(M)/2]
        M2 = M[len(M)/2:]
        return min(last + cost(M1,P1) + cost(M2,P2),
                     cost([x-1 for x in M1], P1) + 
                     cost([x-1 for x in M2], P1))
    return cost(M,PRICES)
################################################################

from datetime import datetime
time_start = datetime.today()
def now(): return datetime.today() - time_start 

import sys
infilename = sys.argv[1]
outfilename = infilename.replace('.in','.out')

input = open(sys.argv[1], 'r')
output = open(sys.argv[1].replace('.in','.out'), 'w')
n = int(input.readline())

for i in range(1,n+1):
    result = solve()
    print "Case #%d: %d \t %s" % (i, result, now())
    output.write("Case #%d: %d\n" % (i, result))
