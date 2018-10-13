#Codejam Problem A. Bot Trust
#Bots can move while the other has been doing nothing

from sys import stdin

cases = int(stdin.readline())

def recurse(a = 0, b = 0, xa = 0, xb = 0, at = 0):
    global result, pile, piles
    if at == piles:
        if xa == xb and a and b:
            return max(a, b)
        return -1

    return max(recurse(a + pile[at], b, xa ^ pile[at], xb, at + 1),
                recurse(a, b + pile[at], xa, xb ^ pile[at], at + 1))
            

for caseNo in xrange(1, cases+1):
    piles = int(stdin.readline())
    pile = [int(x) for x in stdin.readline().split()]
    result = recurse()
    if result == -1:
        print "Case #%d: NO" % caseNo
    else:
        print "Case #%d: %d" % (caseNo, result)
    
